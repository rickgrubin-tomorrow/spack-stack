# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTolColors(PythonPackage):
    """Color schemes for lines and maps, color-blind safe"""

    pypi = 'tol-colors/tol-colors-1.3.0.tar.gz'
    homepage = "https://github.com/Descanonge/tol_colors"
    git = "https://github.com/Descanonge/tol_colors.git"
    url = "https://github.com/Descanonge/tol_colors/archive/refs/tags/v1.2.1.tar.gz"


    maintainers = ["rhoneyager-tomorrow"]

    version("1.3.0", sha256="5276b52df70032e3401b2c8c6c055e676dc05db8bb760155dc555a93318d7a25")
    version("1.2.1", sha256="2c6f7ffe61e3fe553d85b231301c4ed0bdbbcaba75185710f681a29cfc0c790f")

    #depends_on("py-setuptools@0.7.2:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-matplotlib")
    depends_on("py-numpy")

