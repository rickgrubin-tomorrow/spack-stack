# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mirs(CMakePackage):
    """NOAA's Microwave Integrated Retrieval System"""

    homepage = "https://www.star.nesdis.noaa.gov/mirs/index.php"
    git = 'git@github.com:climacell/nwp-mirs.git'

    maintainers = ["rhoneyager-tomorrow"]

    depends_on('hdf5@1.14.3: +fortran +hl')
    depends_on('netcdf-c')
    depends_on('zlib')

    version('11.10.0.1', commit='e918f984e4d25c954aa3f8f399dadc03815382bb')
    version('11.10.0', commit='ef556263cc782fe2b5b8511789126aba94ab8a31')

    def cmake_args(self): 
        res = [
            self.define('MIRS_BUILD_MIRS2NC', False),
            self.define('USE_EXTERNAL_DATA', True),
            self.define('EXTERNAL_DATA_DIR', '/backup2/stacks/mirs/mirs_v11r10_r111024075/data')
        ]
        return res

