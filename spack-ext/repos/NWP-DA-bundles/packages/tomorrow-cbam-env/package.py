# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class TomorrowCbamEnv(BundlePackage):
    """Development environment for CBAM"""

    maintainers("rickgrubin-tomorrow")

    version("1.0.0")

    depends_on("tomorrow-base-env", type=("build", "run"))
    depends_on("tomorrow-wrf-env", type=("build", "run"))
    depends_on("bufr", type="run")
    depends_on("cdo", type="run")
    #depends_on("convert_geotiff", type="run")
    depends_on("g2c", type="run")
    depends_on("gsl", type="run")
    depends_on("hdf", type="run")
    depends_on("libgeotiff", type="run")
    #depends_on("metar", type="run")


    depends_on("madis", type="run")
    depends_on("met", type="run")
    #depends_on("obsgrid", type="run")

    #depends_on("upp", type="run")
    depends_on("wrf-io", type="run")
    depends_on("wrf", type="run")
    depends_on("wps", type="run")
    depends_on("wrfda", type="run")

    # There is no need for install() since there is no code.
