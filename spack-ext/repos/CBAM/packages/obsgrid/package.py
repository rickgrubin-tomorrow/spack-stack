# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import fnmatch
import os
import sys
#import time
#from os.path import basename
from pathlib import Path
#from subprocess import PIPE, Popen

from llnl.util import tty

from spack.package import *

if sys.platform != "win32":
    from fcntl import F_GETFL, F_SETFL, fcntl
    from os import O_NONBLOCK


def setNonBlocking(fd):
    """
    Set the given file descriptor to non-blocking
    Non-blocking pipes are not supported on windows
    """
    flags = fcntl(fd, F_GETFL) | O_NONBLOCK
    fcntl(fd, F_SETFL, flags)


class Obsgrid(Package):
    """The WRF Objective analysis (OA) program is a program
    that blends observations (in the form of ASCII format) and background
    (first guess) fields from WPS/metgrid. It provides a simple way to
    add observations to the incoming data from another model.
    """

    homepage = "https://github.com/climacell/CBAM_OBSGRID"
    git = "git@github.com:climacell/CBAM_OBSGRID.git"
    url="https://github.com/climacell/CBAM_OBSGRID.git"
    version("1.0", branch="master")

    depends_on("netcdf-c")
    depends_on("netcdf-fortran")

    requires(
        "%intel",
        policy="one_of",
        msg="OBSGRID supports only the Intel classic compilers",
    )

    phases = ["configure", "build", "install"]

    def setup_run_environment(self, env):
        env.set("OBSGRID_HOME", self.prefix)
        env.append_path("PATH", self.prefix.main)
        env.append_path("PATH", self.prefix.tools)

    def setup_build_environment(self, env):
        env.set("NETCDF", self.spec["netcdf-c"].prefix)
        env.set("NETCDFF", self.spec["netcdf-fortran"].prefix)

    @run_before("configure")
    def fortran_check(self):
        if not self.compiler.fc:
            msg = "cannot build Obsgrid without a Fortran compiler"
            raise RuntimeError(msg)

    def configure(self, spec, prefix):
        pass

    def run_compile_script(self):
        csh = which("csh")

        # Now run the compile script and track the output to check for
        # failure/success We need to do this because upstream use `make -i -k`
        # and the custom compile script will always return zero regardless of
        # success or failure
        result_buf = csh(
            "./compile",
            "obsgrid",
            output=str,
            error=str,
        )

        print(result_buf)

        # check for obsgrid.exe 
        dir_path = self.stage.source_path + '/src'
        if len(fnmatch.filter(os.listdir(dir_path), '*.exe')) == 1:
            return True

        return False

    def build(self, spec, prefix):
        result = self.run_compile_script()

        if not result:
            raise InstallError("Compile failed. Check the output log for details.")

    def install(self, spec, prefix):
        # Save all install files as many are needed
        install_tree(".", prefix)
