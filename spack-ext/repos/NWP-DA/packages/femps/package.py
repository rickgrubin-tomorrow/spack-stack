# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Femps(CMakePackage):
    """Finite Element Mesh Poisson Solver"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/femps.git'

    maintainers = ["rhoneyager-tomorrow"]

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.7.0:')
    depends_on('jedi-cmake', type=('build'))
    depends_on('llvm-openmp', when='%apple-clang', type=('build', 'run'))
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')

    version('1.3.0', commit='4f12677d345e683bf910b5f76f0df120ad27482d')
    version('1.2.0', commit='a22e458c1742695479db9011ddb6bcbf31de39fe')

    patch('CMakeLists.txt.patch', when='@1.2.0')
    patch('src.femps.CMakeLists.txt.patch', when='@1.2.0')

