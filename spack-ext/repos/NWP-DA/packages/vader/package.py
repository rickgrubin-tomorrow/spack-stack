# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Vader(CMakePackage):
    """The VAriable DErivation Repository"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/vader.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant('gsw', default=True, description='Build gsw recipes')

    depends_on('boost@1.64:', type=('build'), when='@1.6:')
    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.4.0:')
    depends_on('gsw', when='+gsw @1.6:')
    depends_on('jedi-cmake', type=('build'))
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('oops')
    depends_on('oops@1.7.0', when='@1.4.0')
    depends_on('oops@1.8.0', when='@1.5.0')
    depends_on('oops@1.9', when='@1.6')
    depends_on('oops@1.10:', when='@1.7:')

    version('1.7.0', commit='67770f24f615b3d17990550f63592021513cbfb2')
    version('1.6.0', commit='3d90d96a04a58ea194323894bb392fb2fd0d9a76')
    version('1.5.0', commit='17173dc97a727e623e4b54ee06e2a0dc71f643de')
    version('1.4.0', commit='4264b56111a62ab1339320ad85a7f715b923df47')
    version('1.3.0', commit='3297467610cb5ff3e1c44a52515774f52a04b888')
    version('1.2.0', commit='7f02b54c40807c0c7e43b698aba91709e25ffeae')
    version('1.1.0', commit='bbc9e9f329b1d93d09e463b2dccbdbfc964d05d4')
    version('1.0.0', commit='923f9de3f1837ca88ca22180b8ee654b6b3629ae')
    version('develop', branch='develop')
    version('master', branch='master')

