# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Soca(CMakePackage):
    """Sea-Ice Ocean and Coupled Assimilation"""

    homepage = "https://www.jcsda.org/jcsda-project-soca"
    git = 'https://github.com/JCSDA/soca.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant('icepack', default=False, description='Build with icepack support')

    conflicts('+icepack', msg='SOCA: icepack to be implemented.')

    depends_on('ecmwf-atlas@0.35:')
    depends_on('ecbuild@3.3.2:', type=('build'))
    depends_on('eckit@1.23.0:')
    depends_on('eckit@1.24.4:', when='@1.8:')
    depends_on('fckit@0.10.1:')
    depends_on('fckit@0.11:', when='@1.8')
    depends_on('fms@release-jcsda', when='@:1.8')
    #depends_on('fms@2020.4:', when='@1.8:')
    depends_on('gsl-lite')
    depends_on('ioda')
    depends_on('ioda@2.6.0', when='@1.5')
    depends_on('ioda@2.7.0', when='@1.6')
    depends_on('ioda@2.8.0', when='@1.7')
    depends_on('ioda@2.9', when='@1.8')
    depends_on('jedi-cmake', type=('build'))
    depends_on('mom6@2020.4.0:')
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('oops')
    depends_on('oops@1.7', when='@1.5')
    depends_on('oops@1.8', when='@1.6')
    depends_on('oops@1.9.1:1.9', when='@1.7')
    depends_on('oops@1.10', when='@1.8')
    depends_on('saber')
    depends_on('saber@1.7', when='@1.5')
    depends_on('saber@1.8', when='@1.6')
    depends_on('saber@1.9', when='@1.7')
    depends_on('saber@1.10', when='@1.8')
    depends_on('ufo')
    depends_on('ufo@1.7', when='@1.5')
    depends_on('ufo@1.8', when='@1.6')
    depends_on('ufo@1.9', when='@1.7')
    depends_on('ufo@1.10', when='@1.8')
    depends_on('vader')
    depends_on('vader@1.4', when='@1.5')
    depends_on('vader@1.5', when='@1.6')
    depends_on('vader@1.6', when='@1.7')
    depends_on('vader@1.7', when='@1.8')

    #depends_on('icepack', when='+icepack')

    version('1.8.0', commit='5ff26f076fac7b53e7c41547cd2baa39eb2f9b1d')
    version('1.7.0', commit='5783fd72ace301b07a9c264595c82c31e7e872b6')
    version('1.6.0', commit='fc4677b5971e555a6859a5e98f646e660d22d0c9')
    version('1.5.0', commit='27d53e07a055f2ce0695018c6f76b0ba3e4b20e7')
    version('develop', branch='develop')
    version('master', branch='master')

