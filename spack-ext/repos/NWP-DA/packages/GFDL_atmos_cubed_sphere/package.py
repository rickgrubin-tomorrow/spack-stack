# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class GfdlAtmosCubedSphere(CMakePackage):
    """The GFDL atmos_cubed_sphere dynamical core code"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/GFDL_atmos_cubed_sphere.git'

    maintainers = ["rhoneyager-tomorrow"]

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.7.0:')
    depends_on('fms')
    depends_on('jedi-cmake', type=('build'))
    depends_on('llvm-openmp', when='%apple-clang', type=('build', 'run'))
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')

    version('1.2.0.jcsda', commit='61450b4e3e80bb96b26c5f3808ce60b5e5cb4207')

    patch('CMakeLists.txt.patch', when='@1.2.0.jcsda')

