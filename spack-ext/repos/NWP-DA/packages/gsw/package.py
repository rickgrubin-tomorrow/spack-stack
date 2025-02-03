# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gsw(CMakePackage):
    """Gibbs-SeaWater (GSW) Oceanographic Toolbox in Fortran"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/GSW-fortran.git'

    maintainers = ["rhoneyager-tomorrow"]

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@3.0.7:')

    version('3.0.7', commit='1a02ebaf6f7a4e9f2c2d2dd973fb050e697bcc74')
    version('develop', branch='develop')
    version('master', branch='master')

