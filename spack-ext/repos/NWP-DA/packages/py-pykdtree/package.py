# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPykdtree(PythonPackage):
    """Fast kd-tree implementation with OpenMP-enabled queries"""

    pypi = 'pykdtree/pykdtree-1.3.6.tar.gz'

    maintainers = ["rhoneyager"]

    version("1.3.13", sha256="3accf852e946653e399c3d4dbbe119dbc6d3f72cfd2d5a95cabf0bf0c7f924fe")
    version("1.3.12", sha256="cc20b2a67c64056485a314d2c2b6dba354af7ee1c8fb8dae1be6f2936a374341")
    version("1.3.11", sha256="6c123c7bae5213af223c529a8b4161c07eb854a6fe4038b36952bada2131ebcb")
    version("1.3.6", sha256="780b693d0555b857d7aab31e35d4293bf4ebdb9dec7a45ba4bb23b4400f626dc")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-numpy")

    #depends_on("py-setuptools@0.7.2:", type="build")
    #depends_on("py-numpy@1.13:")

