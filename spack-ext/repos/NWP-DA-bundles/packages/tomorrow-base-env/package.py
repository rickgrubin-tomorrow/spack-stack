# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack.package import *


class TomorrowBaseEnv(BundlePackage):
    """Basic development environment used by other environments"""

    homepage = "https://github.com/jcsda/spack-stack"
    git = "https://github.com/jcsda/spack-stack.git"

    maintainers("rhoneyager-tomorrow")

    version("2024.8.21")

    # Basic utilities
    depends_on("libbacktrace", type="run")

    depends_on("cmake", type="run")
    depends_on("curl", type="run")
    depends_on("git", type="run")
    depends_on("wget", type="run")

    depends_on("pkgconfig", type=("build", "run"))

    depends_on("hdf5", type="run")
    depends_on("jasper", type="run")
    depends_on("libpng", type="run")
    depends_on("libjpeg-turbo", type="run")
    depends_on("nccmp", type="run")
    depends_on("nco", type="run")
    depends_on("netcdf-c", type="run")
    depends_on("netcdf-fortran", type="run")
    depends_on("parallel-netcdf", type="run")
    depends_on("parallelio", type="run")
    depends_on("zlib", type="run")

    # Python
    depends_on("python@3.7:", type="run")
    depends_on("py-pip", type="run")
    depends_on("py-wheel", type="run")
    depends_on("py-setuptools", type="run")
    depends_on("py-setuptools-scm", type="run")

    # There is no need for install() since there is no code.
