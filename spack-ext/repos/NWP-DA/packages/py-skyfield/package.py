# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySkyfield(PythonPackage):
    """
    Skyfield is a pure-Python astronomy package that is compatible with both Python 2 and 3 and makes
    it easy to generate high precision research-grade positions for planets and Earth satellites.
    """

    pypi = 'skyfield/skyfield-1.53.tar.gz'

    maintainers = ["rickgrubin-tomorrow"]

    version("1.53", sha256="24099855f3ba3906663ac1c10e650041e747680b986e807400eddedc0be4a8b4")
    version("1.52", sha256="3d0d335a81b8db36d4a658636f211fe51122cda43908ec2573a956ec93e91dec")
    version("1.51", sha256="afebb71a86ff1049885133120f9149a54ed2d8b38721307eeb0e0a93ca73aafc")
    version("1.50", sha256="3dd287fbed42ddcf32bdbf7d12b90cbeaf5f44fcefce700cd49514f5776c66ba")

    depends_on("py-setuptools", type="build")
    depends_on("py-certifi", type="run")
    depends_on("py-jplephem", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-spg4", type="run")
