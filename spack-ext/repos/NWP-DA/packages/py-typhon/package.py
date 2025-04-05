# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTyphon(PythonPackage):
    """ARTS bindings."""

    pypi = 'typhon/typhon-0.9.0.tar.gz'

    maintainers = ["rhoneyager"]

    version("0.10.0", sha256="14dc0adfb772d67f15890863ca6c0d2dce3904b4802351c24c082f69897d393f")
    version("0.9.0", sha256="33d64846cc77d94a969d625a2b8e9a6926ad804a0810ec3667110542555d75b4")

    #depends_on("py-setuptools@0.7.2:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-cartopy", type=("run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-fsspec", type="run")
    depends_on("gdal+python")
    depends_on("py-h5netcdf")
    #depends_on("py-keras")
    depends_on("py-keras@3.9: backend=torch")
    depends_on("py-matplotlib")
    depends_on("py-nbsphinx")
    depends_on("py-netcdf4")
    #depends_on("py-numba") # disabled because it needs an old version of LLVM that no longer compiles.
    depends_on("py-numexpr")
    depends_on("py-numpy")
    depends_on("py-pandas")
    depends_on("py-pint")
    depends_on("py-pytest")
    depends_on("py-pykdtree")
    #depends_on("py-scikit-image")
    depends_on("py-scikit-image@0.23:")
    depends_on("py-scikit-learn")
    depends_on("py-scipy")
    depends_on("py-sphinx")
    depends_on("py-sphinx-rtd-theme")
    depends_on("py-xarray")

