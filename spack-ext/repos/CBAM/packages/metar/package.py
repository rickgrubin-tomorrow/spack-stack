# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Metar(MakefilePackage):
    """
    METAR (Meteorological Aerodrome Report) is a standard weather report used in aviation to
    provide a snapshot of current weather conditions at a specific location.
    """

    homepage = "https://github.com/climacell/CBAM_OBSGRID"
    git = "git@github.com:climacell/CBAM_OBSGRID.git"
    url="https://github.com/climacell/CBAM_OBSGRID.git"
    version("1.0", branch="master")

    def build(self, spec, prefix):
        make("all")

    def install(self, spec, prefix):
        copy_tree("bin", prefix.bin)
        install("stations.txt", prefix)
