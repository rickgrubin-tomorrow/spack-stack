# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Saber(CMakePackage):
    """System-Agnostic Background Error Representation"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/saber.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant('fftw', default=True, description='Enable FFTW FastLAM spectral layer')
    variant('gsibec', default=True, description='Enable SABER block GSI')
    variant('mkl', default=False, description='Use MKL for LAPACK implementation')
    variant('oops', default=True, description='Use oops')
    variant('openmp', default=True, description='Build with OpenMP support')
    variant('vader', default=True, description='Build with vader support')

    conflicts('+fftw', when='@:1.9', msg='fftw is supported only in saber versions 1.10+')
    conflicts('~oops', when='@1.10:', msg='oops is required in saber versions 1.10+')

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.4.0:')
    depends_on('eckit')
    depends_on('eckit@1.23.0', when='@1.7:1.8')
    depends_on('eckit@1.24.4:', when='@1.9:')
    depends_on('ecmwf-atlas')
    depends_on('ecmwf-atlas@0.33.0', when='@1.7:1.8')
    depends_on('ecmwf-atlas@0.35:', when='@1.9:')
    depends_on('ecmwf-atlas+openmp', when='+openmp')
    depends_on('ecmwf-atlas~openmp', when='~openmp')
    depends_on('fckit')
    depends_on('fckit@0.10.1', when='@1.7:1.8')
    depends_on('fckit@0.11:', when='@1.9:')
    depends_on('fftw@3.3.8:', when='@1.10: +fftw')
    depends_on('gsibec', when='+gsibec')
    depends_on('gsibec@1.1.2', when='@1.7:1.8 +gsibec')
    depends_on('gsibec@1.1.3', when='@1.9 +gsibec')
    depends_on('gsibec@1.2.1', when='@1.10: +gsibec')
    depends_on('jedi-cmake', type=('build'))
    depends_on('lapack', when='~mkl')
    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'link', 'run'))
    depends_on('mkl', when='+mkl')
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('oops', when='+oops')
    depends_on('oops+openmp', when='+oops +openmp')
    depends_on('oops~openmp', when='+oops ~openmp')
    depends_on('oops@1.7.0', when='@1.7.0 +oops')
    depends_on('oops@1.8.0', when='@1.8.0 +oops')
    depends_on('oops@1.9', when='@1.9 +oops')
    depends_on('oops@1.10', when='@1.10')
    depends_on('sp', when='+gsibec')
    depends_on('vader', when='+vader')
    depends_on('vader@1.4.0', when='@1.7.0 +vader')
    depends_on('vader@1.5.0', when='@1.8.0 +vader')
    depends_on('vader@1.6', when='@1.9 +vader')
    depends_on('vader@1.7', when='@1.10 +vader')

    version('1.10.0', commit='2deedb07ddd8faf2f9eef8c9278b900df8b55d4f')
    version('1.9.0', commit='767f6a9a1778e34d58a7cfc55f1d6d499ce2f6ea')
    version('1.8.0', commit='de99a5a8130e230e8bb14785f6e3133d7da047b8')
    version('1.7.0', commit='d90ce5276b37552d569fcb72a22b5a30fb03de75')
    version('1.6.0', commit='eba775583475f5ba1411d988b047a94d2c85ac9c')
    version('1.5.0', commit='250e211805d9173105facfda0b9869e418702128')
    version('1.4.0', commit='67d7451d14d92abd70c23a92f6bc8939d70b1bb1')
    version('1.3.0', commit='6ef18352a7f4012fbc366e16a73374d1d9df4bc8')
    version('1.2.0', commit='3090207f710f5ba25831cdd437f7d38a733011c1')
    version('1.1.3', commit='86c530d0a409cdcb1788ce2cc2f912b4b71f8e53')
    version('1.1.2', commit='687d7978c38e94ce9be0b44cb6b6a36981c1a244')
    version('1.1.1', commit='9683ef97c6f42e3c21833c13b766b1e0cc997952')
    version('1.1.0', commit='dc56a401b29152d4b38d409656253af2586dd6b2')
    version('1.0.0', commit='175664c0971fc786eb11a9a369036503141ba21f')
    version('develop', branch='develop')
    version('master', branch='master')

    def cmake_args(self):
        res = [
            self.define_from_variant('ENABLE_MKL', 'mkl'),
            self.define_from_variant('OPENMP',  'openmp')
        ]
        return res

    patch('quench.src.Fields.cc.patch', when='@1.7')
    patch('CMakeLists.txt.patch', when='@1.7:1.9')
    patch('saber-import.cmake.in.patch', when='@1.7:1.9')

