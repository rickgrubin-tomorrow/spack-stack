# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySgp4(PythonPackage):
    """
    SGP4 merges together what in the 1970s were originally two separate satellite propagation routines, 
    but which are now selected automatically:

    SGP4 — the ‘Simplified General Perturbations’ model is used for satellites close enough to Earth that 
    their orbit takes less than 225 minutes (3 hours 45 minutes) to complete.

    SDP4 — the ‘Simplified Deep Space Perturbations’ model is used for satellites farther from Earth, 
    which take 225 minutes or longer to compete an orbit.
    """

    pypi = 'sgp4/sgp4-2.24.tar.gz'
    homepage = "https://github.com/brandon-rhodes/python-sgp4"

    maintainers = ["rickgrubin-tomorrow"]

    version("2.24", sha256="5655249f276ea23fbdae9e881ab01d82420285b45dc76d0da4f424e3647f8352")
    version("2.23", sha256="d8addc53a2fb9f88dee6bfd401d2865b014cc0b57bf2cee69bdee8d9685d5429")
    version("2.22", sha256="17f0a2eaad2dca065b6de25c1ceaa940ff7cfa8cc67120cb4111a00f177b86f9")

    depends_on("py-setuptools", type="build")
