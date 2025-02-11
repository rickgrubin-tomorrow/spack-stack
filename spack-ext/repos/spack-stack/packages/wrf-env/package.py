# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class WrfEnv(BundlePackage):
    """Development environment for WRF"""

    homepage = "https://github.com/NOAA-EMC/GSI"
    git = "https://github.com/NOAA-EMC/GSI.git"

    maintainers("rickgrubin-tomorrow")

    version("1.0.0")

    depends_on("base-env", type=("build", "run"))
    depends_on("bufr", type="run")
    depends_on("cdo", type="run")
    depends_on("g2c", type="run")
    depends_on("gsl", type="run")
    depends_on("libgeotiff", type="run")

    depends_on("netcdf-cxx", type="run")

    depends_on("madis", type="run")
    depends_on("met", type="run")


    depends_on("ncl", type="run")
    depends_on("wrf-io", type="run")

    # There is no need for install() since there is no code.
