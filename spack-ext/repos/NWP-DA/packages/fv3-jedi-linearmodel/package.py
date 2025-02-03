# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fv3JediLinearmodel(CMakePackage):
    """Tangent linear and adjoint versions of FV3 dynamical core and GEOS physics"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/fv3-jedi-linearmodel.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant(
        "forecast_model",
        default="FV3CORE",
        description="fv3 forecast model",
        values=("FV3CORE", "GEOS", "UFS"),
    )
    variant('mkl', default=False, description='Use MKL for LAPACK implementation (if available)')
    variant('mpi', default=True, description='Support for MPI distributed parallelism')
    variant('openmp', default=True, description='Build with OpenMP support')

    conflicts('forecast_model=GEOS', msg='FV3-JEDI-LINEARMODEL: GEOS to be implemented.')
    conflicts('forecast_model=UFS', msg='FV3-JEDI-LINEARMODEL: UFS to be implemented.')

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.3.0:')
    depends_on('ecbuild@3.6:', type=('build'), when='@1.5.0:')
    #depends_on('fms@2023.04:', when='@1.6:')
    #depends_on('fms@release-jcsda', when='@:1.5')
    depends_on('fms@2023.04:', when='forecast_model=FV3CORE @1.6:')
    depends_on('fms@2023.04:', when='forecast_model=UFS @1.6:')
    depends_on('fms@release-jcsda', when='forecast_model=FV3CORE @:1.5')
    depends_on('fms@release-jcsda', when='forecast_model=UFS @:1.5')
    depends_on('jedi-cmake', type=('build'))
    depends_on('lapack', when='~mkl')
    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'link', 'run'))
    depends_on('mkl', when='+mkl')
    depends_on('mpi', when='+mpi')
    depends_on('netcdf-fortran')
    depends_on('netcdf-c~mpi', when='~mpi')
    depends_on('netcdf-c+mpi', when='+mpi')

    # Future: GEOS needs
    # - MAPL (underway at GMAO)
    # - GEOSgcm
    # - fms r8 or r4

    # Future: UFS needs
    # - stochastic_physics
    # - ccpp
    # - ccppphys
    # - fv3atm
    # - ufs
    # - FMS::fms_r8

    # TODO: CMake flags!!!

    version('1.5.0', commit='af67095ee87ffb472218aa386e34c6bfe64ca424')
    version('1.4.0', commit='05cc1ae63252ca535f3db0fdca9a8a996329fc8f')
    version('1.3.0', commit='9758fbd44166fc1e1d745ca9ab7e9e5e6071955f')
    version('1.2.0', commit='d47cea97c659e8a11e9e64c23092bef06227ebde')
    version('develop', branch='develop')
    version('master', branch='master')

    def cmake_args(self):
        res = [
            self.define_from_variant('FV3_FORECAST_MODEL', 'forecast_model')
        ]
        return res

    patch('CMakeLists.txt.patch', when='@1.2:1.4')
    patch('src.CMakeLists.txt.patch', when='@1.2:1.4')

