# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class MpasJedi(CMakePackage):
    """Interface between JEDI and MPAS based models"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/mpas-jedi.git'

    maintainers = ["rhoneyager-tomorrow"]

    # esmf if external. Needs a CMakeLists.txt patch.
    # rttov - optional
    # ropp-ufo - optional
    # saca - optional

    variant('openmp', default=True, description='Build with OpenMP support')

    depends_on('boost')
    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'))
    depends_on('ecmwf-atlas')
    depends_on('ecmwf-atlas@0.23:', when='@3.0')
    depends_on('ecmwf-atlas@0.35:', when='@3.1')
    depends_on('ioda')
    depends_on('ioda@2.8', when='@3.0')
    depends_on('ioda@2.9', when='@3.1')
    depends_on('jedi-cmake', type=('build'))
    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'link', 'run'))
    depends_on('mpas-model-jedi')
    depends_on('mpas-model-jedi@7.0.jcsda3', when='@3')
    depends_on('mpi')
    depends_on('oops')
    depends_on('oops+openmp', when='+openmp')
    depends_on('oops~openmp', when='~openmp')
    depends_on('oops@1.9:', when='@3.0')
    depends_on('oops@1.10', when='@3.1')
    depends_on('saber')
    depends_on('saber@1.9', when='@3.0')
    depends_on('saber@1.10', when='@3.1')
    depends_on('ufo')
    depends_on('ufo@1.9', when='@3.0')
    depends_on('ufo@1.10', when='@3.1')

    version('3.1.0', commit='b05db549add4a299da80f382392540f02cb54533')
    version('3.0.0', commit='be0ffe957df81494756cc4900d21ea14dc21edab')
    version('develop', branch='develop')

    def cmake_args(self):
        spec = self.spec

        cmake_args = []
        if spec.satisfies("^mpas-model-jedi precision=double"):
            cmake_args.append("-DMPAS_DOUBLE_PRECISION:BOOL=ON")
        else:
            cmake_args.append("-DMPAS_DOUBLE_PRECISION:BOOL=OFF")

        return cmake_args

    patch('tests.patch', when='@3')

