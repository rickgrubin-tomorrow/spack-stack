# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import fnmatch
import os
import sys
#from pathlib import Path

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


class LittleR(Package):
    """LITTLE_R is an ASCII-based observation file format, in use since the MM5 era."""

    homepage = "https://www2.mmm.ucar.edu/wrf/users/wrfda/OnlineTutorial/Help/littler.html"
    git = "git@github.com:climacell/CBAM_LittleR.git"
    url="https://github.com/climacell/CBAM_LittleR"
    version("1.0", branch="master")

    depends_on("bufr")
    depends_on("madis")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("wrfda")

    requires(
        "%intel", "%gcc",
        policy="one_of",
        msg="LittleR supports the Intel classic or gcc compilers",
    )

    phases = ["configure", "build", "install"]

    def setup_run_environment(self, env):
        env.set("LITTLE_R_HOME", self.prefix)
        env.append_path("PATH", self.prefix.main)
        env.append_path("PATH", self.prefix.tools)

    def setup_build_environment(self, env):
        env.set("BUFR_EXT", self.spec["wrfda"].prefix + "/var/external/bufr")
        env.set("MADIS_ROOT", self.spec["madis"].prefix)
        env.set("NETCDF_C", self.spec["netcdf-c"].prefix)
        env.set("NETCDF_F", self.spec["netcdf-fortran"].prefix)
        #env.set("WRFDA", self.spec["wrfda"].prefix)

    @run_before("configure")
    def fortran_check(self):
        if not self.compiler.fc:
            msg = "cannot build Obsgrid without a Fortran compiler"
            raise RuntimeError(msg)

    def configure(self, spec, prefix):
        pass

    def run_compile_script(self):
        bash = which("bash")

        # Now run the compile script and track the output to check for
        # failure/success We need to do this because upstream use `make -i -k`
        # and the custom compile script will always return zero regardless of
        # success or failure
        result_buf = bash(
            "./build.sh",
            output=str,
            error=str,
        )

        print(result_buf)

        # check for obsgrid.exe 
        dir_path = self.stage.source_path + '/bin'
        if len(fnmatch.filter(os.listdir(dir_path), '*.exe')) == 5:
            return True

        return False

    def build(self, spec, prefix):
        result = self.run_compile_script()

        if not result:
            raise InstallError("Compile failed. Check the output log for details.")

    def install(self, spec, prefix):
        with working_dir(self.build_directlry):
            copy_tree("bin", prefix.bin)
            #install_tree(".", prefix)
