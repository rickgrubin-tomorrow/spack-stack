# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mom6(CMakePackage):
    """Modular ocean model"""

    homepage = "https://www.jcsda.org/jcsda-project-soca"
    git = 'https://github.com/JCSDA/MOM6.git'

    maintainers = ["rhoneyager-tomorrow"]

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.7.0:')
    depends_on('fms') # Let's let soca control the selected version.
    #depends_on('fms@2020.4.0:')
    #depends_on('fms@release-jcsda')
    depends_on('gsw@3.0.5:')
    depends_on('llvm-openmp', when='%apple-clang', type=('build', 'link', 'run'))
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')

    version('2022.1.0', commit='51ec489ad7d8a86762bef4c46eabd9af5fc41fa4', submodules=True)
    version('develop', branch='develop', submodules=True)
    version('master', branch='master', submodules=True)

