# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fv3Jedi(CMakePackage):
    """Interface between JEDI and FV3 based models"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/fv3-jedi.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant(
        "forecast_model",
        default="FV3CORE",
        description="fv3 forecast model",
        values=("FV3CORE", "GEOS", "UFS"),
    )
    variant('geos-aero', default=False, description='Enable usage of geos-aero')
    variant('gsibec', default=True, description='FV3-SABER block GSI')
    variant('mpi', default=True, description='Support for MPI distributed parallelism')
    variant('openmp', default=True, description='Build with OpenMP support')
    variant('ropp', default=False, description='Enable usage of ropp')
    variant('sp', default=True, description='Enable usage of ncep-sp')

    conflicts('forecast_model=GEOS', msg='FV3-JEDI: GEOS to be implemented.')
    conflicts('forecast_model=UFS', msg='FV3-JEDI: UFS to be implemented.')
    conflicts('+geos-aero', msg='FV3-JEDI: geos-aero to be implemented.')
    conflicts('+ropp', msg='FV3-JEDI: ropp to be implemented.')

    # Note: Although CRTM is mentioned in CMakeLists.txt, it is never explicitly
    # linked within fv3-jedi. Instead, it is only used transitively through ufo.
    depends_on('crtm')
    depends_on('crtm@2.2.3:', when='@:1.5')
    depends_on('crtm@v3.0.0-skylabv5-1', when='@1.6')
    depends_on('crtm@v3.0.0-skylabv6', when='@1.7')
    depends_on('crtm@v3.1.0-skylabv7', when='@1.8')
    depends_on('crtm@v3.1.0-skylabv8-2', when='@1.9')
    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.6:')
    depends_on('ecmwf-atlas')
    depends_on('ecmwf-atlas@0.33.0', when='@1.6:1.7')
    depends_on('ecmwf-atlas@0.35.0:', when='@1.8:')
    depends_on('femps@1.0.0:1.2', when='@1.0:1.8')
    depends_on('femps@1.3.0:', when='@1.9:')
    depends_on('jedi-cmake', type=('build'))
    depends_on('netcdf-fortran')
    depends_on('netcdf-c~mpi', when='~mpi')
    depends_on('netcdf-c+mpi', when='+mpi')
    depends_on('oops')
    depends_on('oops@1.7', when='@1.6')
    depends_on('oops@1.8', when='@1.7')
    depends_on('oops@1.9', when='@1.8')
    depends_on('oops@1.10:', when='@1.9')
    depends_on('saber')
    depends_on('saber@1.7', when='@1.6')
    depends_on('saber@1.8', when='@1.7')
    depends_on('saber@1.9', when='@1.8')
    depends_on('saber@1.10', when='@1.9')
    depends_on('ufo')
    depends_on('ufo@1.7', when='@1.6')
    depends_on('ufo@1.8', when='@1.7')
    depends_on('ufo@1.9', when='@1.8')
    depends_on('ufo@1.10', when='@1.9')
    depends_on('vader')
    depends_on('vader@1.4', when='@1.6')
    depends_on('vader@1.5', when='@1.7')
    depends_on('vader@1.6', when='@1.8')
    depends_on('vader@1.7', when='@1.9')

    depends_on('fms@release-jcsda', when='@:1.9 forecast_model=FV3CORE')
    depends_on('fms@2023.04:', when='@1.10: forecast_model=FV3CORE')

    #depends_on('fv3', when='forecast_model=UFS')

    #depends_on('geos-aero', when='+geos-aero')
    #depends_on('geos-aero@0.0.0', when='@1.7.0 +geos-aero')

    depends_on('fv3-jedi-linearmodel', when='forecast_model=FV3CORE')
    depends_on('fv3-jedi-linearmodel@1.2', when='@1.6 forecast_model=FV3CORE')
    depends_on('fv3-jedi-linearmodel@1.3', when='@1.7 forecast_model=FV3CORE')
    depends_on('fv3-jedi-linearmodel@1.4', when='@1.8 forecast_model=FV3CORE')
    depends_on('fv3-jedi-linearmodel@1.5', when='@1.9 forecast_model=FV3CORE')

    depends_on('GFDL_atmos_cubed_sphere', when='forecast_model=FV3CORE')

    depends_on('gsibec', when='+gsibec')
    depends_on('gsibec@1.1.2:1.1', when='@1.6:1.8 +gsibec')
    depends_on('gsibec@1.2.1:', when='@1.9: +gsibec')

    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'link', 'run'))
    depends_on('mpi', when='+mpi')

    #depends_on('ropp', when='+ropp')
    #depends_on('ropp@0.0.0', when='@1.8: +ropp')
    # TODO: ropp-ufo.

    depends_on('sp', when='+sp')

    version('1.9.0', commit='821ac6243aaad771386bf1cac0007e226c55d67a')
    version('1.8.0', commit='8a4974fa03b7abd267497313cd765fed08bc2623')
    version('1.7.0', commit='75fa0544ae7c6b5446460bef8cb7663f3fe1acad')
    version('1.6.0', commit='3c20ebd2657d4b8df35103207a1e83535b67469c')
    version('1.5.0', commit='6da374ea8f4d565dac75555a2bcc985b4d340fdb')
    version('1.4.0', commit='68d40b82c390ecde5af0ec92c8363e337d577db6')
    version('1.3.0', commit='df9719672adaf3d2fc54937fff18ca024087165b')
    version('1.2.0', commit='f2fede52b08d82d57a92d8dee9d19fd9f7cf9e86')
    version('1.1.0', commit='c623fd4b35120723f9d833eabb1ae11722892848')
    version('1.0.0', commit='6b0b1806c9ac3d9262301465cb4483972e83a33f')
    version('develop', branch='develop')
    version('master', branch='master')

    def cmake_args(self):
        res = [
            self.define_from_variant('FV3_FORECAST_MODEL', 'forecast_model'),
            self.define_from_variant('OPENMP',  'openmp')
        ]
        return res

    # Missing find_package ecbuild
    patch('CMakeLists.txt.16.patch', when='@1.6:1.7')
    # Same as above (different line numbers), and disabling tests
    patch('CMakeLists.txt.18.patch', when='@1.8')
    # Only disable tests
    patch('CMakeLists.txt.19.patch', when='@1.9')

    patch('test.CMakeLists.txt.patch', when='@1.6:1.7')
    patch('cmake.fv3jedi_extra_macros.cmake.patch', when='@1.6:1.8')


