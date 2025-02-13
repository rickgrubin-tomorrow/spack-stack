# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import re
import sys
import time
from os.path import basename
from pathlib import Path
from subprocess import PIPE, Popen

from llnl.util import tty

from spack.package import *

if sys.platform != "win32":
    from fcntl import F_GETFL, F_SETFL, fcntl
    from os import O_NONBLOCK

re_optline = re.compile(r"\s+[0-9]+\..*\((serial|smpar|dmpar|dm\+sm)\)\s+")
re_paroptname = re.compile(r"\((serial|smpar|dmpar|dm\+sm)\)")
re_paroptnum = re.compile(r"\s+([0-9]+)\.\s+\(")
re_nestline = re.compile(r"\(([0-9]+=[^)0-9]+)+\)")
re_nestoptnum = re.compile(r"([0-9]+)=")
re_nestoptname = re.compile(r"=([^,)]+)")


def setNonBlocking(fd):
    """
    Set the given file descriptor to non-blocking
    Non-blocking pipes are not supported on windows
    """
    flags = fcntl(fd, F_GETFL) | O_NONBLOCK
    fcntl(fd, F_SETFL, flags)


def collect_platform_options(stdoutpipe):
    # Attempt to parse to collect options
    optiondict = {}
    for line in stdoutpipe.splitlines():
        if re_optline.match(line):
            numbers = re_paroptnum.findall(line)
            entries = re_paroptname.findall(line)
            paropts = dict(zip(entries, numbers))
            platline = re_optline.sub("", line).strip()
            optiondict[platline] = paropts

    return optiondict


def collect_nesting_options(stdoutpipe):
    nestoptline = re_nestline.search(stdoutpipe)[0]
    nestoptnum = re_nestoptnum.findall(nestoptline)
    nestoptname = re_nestoptname.findall(nestoptline)
    nestoptname = [x.replace(" ", "_") for x in nestoptname]

    return dict(zip(nestoptname, nestoptnum))


class Obsgrid(Package):
    """The WRF Objective analysis (OA) program is a program
    that blends observations (in the form of ASCII format) and background
    (first guess) fields from WPS/metgrid. It provides a simple way to
    add observations to the incoming data from another model.
    """

    homepage = "https://github.com/wrf-model/OBSGRID" 
    git = "https://github.com/wrf-model/OBSGRID.git"
    version("1.0", branch="master")
    #version("master", git = "https://github.com/wrf-model/OBSGRID.git")
    #version("1.0", sha256="d8e145e56182a1d76ede4f934e7565c99073def4780f692aed5bb84d130afd74")

    patch("obs_sort_module.F90.patch")

    depends_on("netcdf-c")
    depends_on("netcdf-fortran")

    requires(
        "%gcc",
        "%intel",
        "%oneapi",
        policy="one_of",
        msg="OBSGRID supports only the GCC, Intel, oneAPI compilers",
    )

    phases = ["configure", "build", "install"]

    def setup_run_environment(self, env):
        env.set("OBSGRID_HOME", self.prefix)
        env.append_path("PATH", self.prefix.main)
        env.append_path("PATH", self.prefix.tools)

    def setup_build_environment(self, env):
        env.set("NETCDF", self.spec["netcdf-fortran"].prefix)
        env.set("NETCDF_C", self.spec["netcdf-c"].prefix)
        #env.set("NETCDF", self.spec["netcdf-c"].prefix)

        if "+netcdf_classic" in self.spec:
            env.set("NETCDF_classic", 1)
        # This gets used via the applied patch files
        env.set("NETCDFF", self.spec["netcdf-fortran"].prefix)

    def flag_handler(self, name, flags):
        # Force FCFLAGS/FFLAGS by adding directly into spack compiler wrappers.
        flags.extend(["-fallow-argument-mismatch", "-fallow-invalid-boz"])
        return (flags, None, None)

    def answer_configure_question(self, outputbuf):
        # Platform options question:
        if "Please select from among the following" in outputbuf:
            options = collect_platform_options(outputbuf)
            comp_pair = "%s/%s" % (
                basename(self.compiler.fc).split("-")[0],
                basename(self.compiler.cc).split("-")[0],
            )
            compiler_matches = dict((x, y) for x, y in options.items() if comp_pair in x.lower())
            if len(compiler_matches) > 1:
                tty.warn("Found multiple potential build options")
            try:
                compiler_key = min(compiler_matches.keys(), key=len)
                tty.warn("Selected build option %s." % compiler_key)
                return (
                    "%s\n" % compiler_matches[compiler_key][self.spec.variants["build_type"].value]
                )
            except KeyError:
                InstallError(
                    "build_type %s unsupported for %s compilers"
                    % (self.spec.variants["build_type"].value, comp_pair)
                )

    @run_before("configure")
    def fortran_check(self):
        if not self.compiler.fc:
            msg = "cannot build WRF without a Fortran compiler"
            raise RuntimeError(msg)

    def configure(self, spec, prefix):
        p = Popen(["./configure"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        if sys.platform != "win32":
            setNonBlocking(p.stdout)
            setNonBlocking(p.stderr)

        # Because of WRFs custom configure scripts that require interactive
        # input we need to parse and respond to questions.  The details can
        # vary somewhat with the exact version, so try to detect and fail
        # gracefully on unexpected questions.
        stallcounter = 0
        outputbuf = ""
        while True:
            line = p.stderr.readline().decode()
            if not line:
                line = p.stdout.readline().decode()
            if not line:
                if p.poll() is not None:
                    returncode = p.returncode
                    break
                if stallcounter > 300:
                    raise InstallError(
                        "Output stalled for 30s, presumably an " "undetected question."
                    )
                time.sleep(0.1)  # Try to do a bit of rate limiting
                stallcounter += 1
                continue
            sys.stdout.write(line)
            stallcounter = 0
            outputbuf += line
            if "Enter selection" in outputbuf or "Compile for nesting" in outputbuf:
                answer = self.answer_configure_question(outputbuf)
                p.stdin.write(answer.encode())
                p.stdin.flush()
                outputbuf = ""

        if returncode != 0:
            raise InstallError("Configure failed - unknown error")

    def run_compile_script(self):
        csh_bin = self.spec["tcsh"].prefix.bin.csh
        csh = Executable(csh_bin)

        # num of compile jobs capped at 20 in wrf
        num_jobs = str(min(int(make_jobs), 20))

        # Now run the compile script and track the output to check for
        # failure/success We need to do this because upstream use `make -i -k`
        # and the custom compile script will always return zero regardless of
        # success or failure
        result_buf = csh(
            "./compile",
            "-j",
            num_jobs,
            self.spec.variants["compile_type"].value,
            output=str,
            error=str,
        )

        print(result_buf)
        if "Executables successfully built" in result_buf:
            return True

        return False

    def build(self, spec, prefix):
        result = self.run_compile_script()

        if not result:
            tty.warn("Compilation failed first time (WRF idiosyncrasies?) " "- trying again...")
            result = self.run_compile_script()

        if not result:
            raise InstallError("Compile failed. Check the output log for details.")

    def install(self, spec, prefix):
        # Save all install files as many are needed for WPS and WRF runs
        install_tree(".", prefix)
