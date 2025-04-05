# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack import *


class PmwRadsimEnv(BundlePackage):
    """RadSim development environment."""

    homepage = "https://github.com/climacell/spack-stack"
    git      = "https://github.com/climacell/spack-stack.git"

    maintainers = ['rhoneyager-tomorrow']

    version('2023.9.28')

    #depends_on('rttov', type='run')
    depends_on('spacerad', type='run')
    depends_on('PyTMatrix', type='run')

    depends_on('python@3.7:')
    depends_on('py-boto3', type='run')
    depends_on('py-cartopy', type='run')
    depends_on('py-h5py', type='run')
    depends_on('py-matplotlib', type='run')
    depends_on('py-netcdf4', type='run')
    depends_on('py-numpy', type='run')
    depends_on('py-progressbar2', type='run')
    depends_on('py-pysolar', type='run')
    depends_on('py-scikit-learn', type='run')
    depends_on('py-scipy', type='run')
    depends_on('py-rich', type='run')
    depends_on('py-tol-colors', type='run')
    #depends_on('py-thompson-microphys', type='run') # Local
    depends_on('py-tqdm', type='run')
    #depends_on('py-typhon', type='run')
    depends_on('py-zarr', type='run')

    # from NPW-DA/packages/py-typhon
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-fsspec", type="run")
    #depends_on("gdal +python")
    depends_on("py-h5netcdf")
    depends_on("py-nbsphinx")
    depends_on("py-numexpr")
    depends_on("py-pandas")
    depends_on("py-pint")
    depends_on("py-pytest")
    depends_on("py-pykdtree")
    depends_on("py-scikit-image@0.23:")
    depends_on("py-sphinx")
    depends_on("py-sphinx-rtd-theme")
    depends_on("py-xarray")

