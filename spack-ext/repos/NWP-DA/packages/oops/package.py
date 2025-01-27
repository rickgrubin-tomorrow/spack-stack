# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Oops(CMakePackage):
    """Object Oriented Prediction System"""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA/oops.git'

    maintainers = ["rhoneyager-tomorrow"]

    variant('l95', default=True, description='Build LORENZ95 toy model')
    variant('qg', default=True, description='Build QG toy model')
    variant('mkl', default=False, description='Use MKL for LAPACK implementation (if available)')
    #variant('gptl', default=False, description='Use GPTL profiling library (if available)')
    #variant('autoprofiling', default=False, description='Enable function-based autoprofiling with GPTL (if available)')
    variant('openmp', default=True, description='Build oops with OpenMP support')

    depends_on('boost@1.64:')
    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.7:1.8')
    depends_on('eckit')
    depends_on('eckit@1.23.0', when='@1.7:1.8')
    depends_on('eckit@1.24.4', when='@1.9:')
    depends_on('ecmwf-atlas')
    depends_on('ecmwf-atlas@0.33.0', when='@1.7:1.8')
    depends_on('ecmwf-atlas@0.35.0:', when='@1.9:')
    depends_on('eigen')
    depends_on('fckit')
    depends_on('fckit@0.10.1', when='@1.7:1.8')
    depends_on('fckit@0.11.0:', when='@1.9:')
    #depends_on('gptl', when='+gptl')
    depends_on('jedi-cmake', type=('build'))
    depends_on('lapack', when='~mkl')
    depends_on('mkl', when='+mkl')
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('nlohmann-json')
    depends_on('nlohmann-json-schema-validator')
    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'link', 'run'))

    version('1.10.0', commit='9953118d64015317bb4a6c5e86c2b8f1026498ad')
    version('1.9.1', commit='60f93924fe446714fcb04d96f6930a760db74b23')
    version('1.8.0', commit='d9c7c74e4597172bf8a69d8585df5ad6d0112e0c')
    version('1.7.0', commit='2426c2040e9ae138c4bf8362cacca84d66bd64bf')
    version('1.6.0', commit='4f232fadf782326e2718c7cc55194511a6409476')
    version('1.5.0', commit='89f0441e13c8f78edb1ae6df05c2206890176061')
    version('1.4.0', commit='9548ed453ba8043d11b03556f7f114cbf8e19da3')
    version('1.3.0', commit='6ddf12e6a28e9b44251e08b86cd688e19d8c76ae')
    version('1.2.0', commit='9875a45dd8c31d393f3bca9dd4191e3754854031')
    version('1.1.0', commit='0a07af4672732aed1d2a279519670064696bcfbe')
    version('1.0.0', commit='40e85e4772d395ea3df2ed29ad660f35c0d7dcb5')
    version('develop', branch='develop')
    version('master', branch='master')

    # Patch fix for v1.3.0 CMakeLists.txt
    patch("oops-1.3.0-CMakeLists.patch", when="@:1.3.0")

    def cmake_args(self):
        res = [
            self.define_from_variant('ENABLE_LORENZ95_MODEL', 'l95'),
            self.define_from_variant('ENABLE_QG_MODEL', 'qg'),
            self.define_from_variant('ENABLE_MKL', 'mkl'),
            self.define_from_variant('OPENMP',  'openmp')
        ]
        return res

