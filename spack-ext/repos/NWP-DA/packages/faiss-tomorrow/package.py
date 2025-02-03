# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class FaissTomorrow(CMakePackage, CudaPackage):
    """Faiss is a library for efficient similarity search and clustering of
     dense vectors.

    Faiss contains algorithms that search in sets of vectors of any size, up
    to ones that possibly do not fit in RAM. It also contains supporting code
    for evaluation and parameter tuning. Faiss is written in C++ with
    complete wrappers for Python/numpy. Some of the most useful algorithms
    are implemented on the GPU. It is developed by Facebook AI Research.
    """

    homepage = "https://github.com/facebookresearch/faiss"
    url = "https://github.com/facebookresearch/faiss/archive/v1.6.3.tar.gz"
    git = "https://github.com/facebookresearch/faiss.git"

    maintainers = ["rhoneyager-tomorrow"]

    version("1.7.2", commit="c08cbff1a4d6c9afb6b8f69004c5530aaf80237a")

    variant("c", default=True, description="Build C API")
    variant("gpu", default=False, description="Build CUDA")
    variant("python", default=False, description="Build Python bindings")

    depends_on("blas")
    depends_on("llvm-openmp", when="%apple-clang")

    depends_on("python@3.7:", when="+python", type=("build", "run"))
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-wheel", when="+python", type="build")
    depends_on("py-numpy", when="+python", type=("build", "run"))
    #depends_on("py-scipy", when="+tests", type=("build", "run"))

    depends_on("python", when="+python", type="build")
    depends_on("py-setuptools", when="+python", type="build")
    depends_on("swig", when="+python", type="build")

    def cmake_args(self):
        res = [
            self.define_from_variant('FAISS_ENABLE_GPU', 'gpu'),
            self.define_from_variant('FAISS_ENABLE_PYTHON', 'python'),
            self.define_from_variant('FAISS_ENABLE_C_API', 'c')
        ]
        return res

