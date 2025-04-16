# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack.package import *


class TomorrowWrfEnv(BundlePackage):
    """Basic development environment used by other environments"""

    homepage = "https://github.com/jcsda/spack-stack"
    git = "https://github.com/jcsda/spack-stack.git"

    maintainers("rickgrubin-tomorrow")

    version("1.0.0")

    depends_on("tomorrow-base-env", type=("build", "run"))

    depends_on("bufr", type="run")
    depends_on("wrf-io", type="run")
    depends_on("wrf", type="run")
    depends_on("wps", type="run")
    #depends_on("wrfda", type="run")

    # There is no need for install() since there is no code.
