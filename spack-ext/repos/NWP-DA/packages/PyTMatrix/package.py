# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Pytmatrix(PythonPackage):
    """Python code for T-matrix scattering calculations"""

    homepage = "https://github.com/jleinonen/pytmatrix"
    git = "https://github.com/jleinonen/pytmatrix.git"
    url = "https://github.com/jleinonen/pytmatrix/archive/refs/tags/0.3.2.tar.gz"

    maintainers = ['rhoneyager-tomorrow']

    version("0.3.2", commit="592cb46eba78fa02b70031884070564f83e8775f")

    depends_on("py-numpy", type="build")
    depends_on("py-scipy", type="build")
    depends_on("py-setuptools", type="build")

