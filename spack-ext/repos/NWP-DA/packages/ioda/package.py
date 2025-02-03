# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ioda(CMakePackage):
    """Interface for Observation Data Access"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/ioda.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant('odc', default=True, description='Build ODC bindings')
    variant('openmp', default=True, description='Build with OpenMP support')

    depends_on('boost@1.64.0:')
    depends_on('ecbuild', type=('build'))
    depends_on('eckit')
    depends_on('eckit@1.23.0:', when='@2.6:')
    depends_on('eigen')
    depends_on('fckit')
    depends_on('fckit@0.10.1:', when='@2.6:')
    depends_on('gsl-lite')
    depends_on('hdf5@1.12.0: +mpi')
    depends_on('hdf5@1.14.0: +mpi', when='@2.6.0:')
    depends_on('jedi-cmake', type=('build'))
    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'link', 'run'))
    depends_on('mpi')
    depends_on('odc', when='+odc')
    depends_on('odc@1.0.2:', when='@2.6: +odc')
    depends_on('odc@1.4.6:', when='@2.8: +odc')
    depends_on('oops+openmp', when='+openmp')
    depends_on('oops~openmp', when='~openmp')
    depends_on('oops@1.7', when='@2.6')
    depends_on('oops@1.8', when='@2.7')
    depends_on('oops@1.9', when='@2.8')
    depends_on('oops@1.10', when='@2.9:')
    depends_on('python@3.7:')
    depends_on('py-pybind11')
    depends_on('udunits@2.2.0:')

    version('2.9.0', commit='7cac6e837151bb86220f59eae4fcd6a456b50ad1')
    version('2.8.0', commit='1ee94a863d1fc8c2752e5b95409d6742f4402f5b')
    version('2.7.0', commit='ee35b7f7f859b78e823b69d72b4bc230b15f3d46')
    version('2.6.0', commit='26abb62ca8d30cc7b84303c4d780f0f253b287c9')
    version('2.5.0', commit='ae1a822909732def18229e981a838ec2796646d6')
    version('2.4.0', commit='18bdbbaac55a76b28a6870d06cc7927b4910cc6d')
    version('2.3.0', commit='9b96b2d2f29f454fe71bcf587be38d6da36125b7')
    version('2.2.0', commit='bb0f0381012222b80d1ec887905f8364a0de93f0')
    version('2.1.0', commit='0190ba2358cca7c7ef5ee697f5c891afbdde5d9c')
    version('2.0.2', commit='5bd372e548eb61d5f7b56a0b3d4cf0ca05e49e75')
    version('1.0.0', commit='3cbf1449f6a2caac946232d91d473a70585054c7')
    version('develop', branch='develop')
    version('master', branch='master')

