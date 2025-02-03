# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ufo(CMakePackage):
    """Unified Forward Operator"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/ufo.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant('crtm', default=True, description='Build CRTM operator')
    variant('geos-aero', default=False, description='Build GEOS-AERO AOD operator')
    variant('gsw', default=True, description='Build marine observation operators')
    variant('oasim', default=False, description='Build with Ocean Atmosphere Spectral Irradiance Model')
    variant('ropp', default=False, description='Build ROPP operator')
    variant('rttov', default=False, description='Build RTTOV operator')

    conflicts('+geos-aero', msg='UFO: GEOS-AERO to be implemented.')
    conflicts('+oasim', msg='UFO: OASIM to be implemented.')
    conflicts('+ropp', msg='UFO: ROPP to be implemented.')
    conflicts('+rttov', msg='UFO: RTTOV to be implemented.')

    depends_on('boost')
    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.7.0:')
    depends_on('eckit')
    depends_on('eckit@1.23.0:', when='@1.7:')
    depends_on('eckit@1.24.4:', when='@1.10:')
    depends_on('eigen')
    depends_on('fckit')
    depends_on('fckit@0.10.1:', when='@1.7:')
    depends_on('fckit@0.11.0:', when='@1.10:')
    depends_on('gsl-lite')
    depends_on('ioda')
    depends_on('ioda@2.6.0', when='@1.7.0')
    depends_on('ioda@2.7.0', when='@1.8.0')
    depends_on('ioda@2.8.0', when='@1.9')
    depends_on('ioda@2.9', when='@1.10')
    depends_on('jedi-cmake', type=('build'))
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('oops')
    depends_on('oops@1.7.0', when='@1.7.0')
    depends_on('oops@1.8.0', when='@1.8.0')
    depends_on('oops@1.9.1:1.9', when='@1.9')
    depends_on('oops@1.10', when='@1.10')

    depends_on('crtm', when='+crtm')
    depends_on('crtm@v3.0.0-skylabv5-1', when='@1.7.0 +crtm')
    depends_on('crtm@v3.0.0-skylabv6', when='@1.8.0 +crtm')
    depends_on('crtm@v3.1.0-skylabv7', when='@1.9 +crtm')
    # skylabv8-1 tag had problems with atms
    depends_on('crtm@v3.1.0-skylabv8-2', when='@1.10 +crtm')
    # Note: CRTM may be decoupled as of 1.8. Check.

    #depends_on('geos-aero', when='+geos-aero')
    #depends_on('geos-aero@0.0.0', when='@1.7: +geos-aero')

    #depends_on('oasim', when='+oasim')
    #depends_on('oasim@0.0.0', when='@1.7: +oasim')

    depends_on('gsw', when='+gsw')
    depends_on('gsw@3.0.7', when='@1.7: +gsw')

    #depends_on('ropp', when='+ropp')
    #depends_on('ropp@0.0.0', when='@1.7: +ropp')

    #depends_on('rttov', when='+rttov')
    #depends_on('rttov@12.1.0', when='@1.7: +rttov')

    version('1.10.0', commit='a306d47194e4147bd53edbde984a5e6a262b74be')
    version('1.9.0', commit='e41a1c928150944795ed1276c84c4f1e37a47c99')
    version('1.8.0', commit='7f7b65bf70e795c4ad02175b606cb18fe5dd4388')
    version('1.7.0', commit='1d745701806bd2a3f3d194c9de87ea7ca0a4c2ab')
    version('1.6.0', commit='64e34207b0fe5e046359a8bab7bb3870787e1214')
    version('1.5.0', commit='3b9a48d975611e8e293e7f2722e8d81fc6716e0a')
    version('1.4.0', commit='552be6c93cc672bf109719b36895a5ef585e0508')
    version('1.3.0', commit='ee4029ba19461bdfdf7022852502f75439f02bc7')
    version('1.2.0', commit='69a6475f478306dd4d4f6728705fe0cd205752c7')
    version('1.1.0', commit='2af9b91433553ca473c72fcd131400a01c3aabdb')
    version('1.0.0', commit='68dab85486f5d79991956076ac6b962bc1a0c5bd')
    version('develop', branch='develop')
    version('master', branch='master')

