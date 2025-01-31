# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack.package import *


class TomorrowBaseEnv(BundlePackage):
    """Basic development environment used by other environments"""

    homepage = "https://github.com/jcsda/spack-stack"
    git = "https://github.com/jcsda/spack-stack.git"

    maintainers("rhoneyager-tomorrow")

    version("2024.8.21")

    # Variants
    variant("hdf4", default=True, description="Build hdf4 library and python hdf module")
    variant("mapl", default=True, description="Build MAPL")

    # Basic utilities
    depends_on("libbacktrace", type="run")

    #depends_on("cmake", type="run")
    #depends_on("curl", type="run")
    #depends_on("git", type="run")
    #depends_on("wget", type="run")
    depends_on("base-env", type="run")

    # I/O
    depends_on("hdf-eos2", type="run", when="+hdf4")
    depends_on("madis", type="run")

    # Utilities
    depends_on("bufr", type="run")
    depends_on("cdo", type="run")
    depends_on("esmf", type="run")
    depends_on("g2c", type="run")
    depends_on("gsl", type="run")
    depends_on("jasper", type="run")
    depends_on("libgeotiff", type="run")
    depends_on("libjpeg", type="run")
    depends_on("libjpeg-turbo", type="run")
    depends_on("libpng", type="run")
    depends_on("met", type="run")
    depends_on("metplus", type="run")
    depends_on("nco", type="run")
    depends_on("ninja", type="run")
    depends_on("rsync", type="run")
    depends_on("sfcio", type="run")

    # Python
    depends_on("py-black", type="run")
    depends_on("py-bokeh", type="run")
    depends_on("py-boto3", type="run")
    depends_on("py-cartopy", type="run")
    depends_on("py-click", type="run")
    depends_on("py-contourpy", type="run")
    depends_on("py-coverage", type="run")
    # depends_on("py-cylc-flow", type="run")
    # depends_on("py-cylc-rose", type="run")
    # depends_on("py-cylc-uiserver", type="run")
    depends_on("py-dask", type="run")
    depends_on("py-flake8", type="run")
    depends_on("py-geopandas", type="run")
    depends_on("py-gitpython", type="run")
    depends_on("py-h5py", type="run")
    depends_on("py-jinja2", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-nbconvert", type="run")
    depends_on("py-netcdf4", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-pandas", type="run")
    #depends_on("py-pip", type="run")
    depends_on("py-pkgconfig", type="run")
    depends_on("py-progressbar2", type="run")
    depends_on("py-pycodestyle@2.10:", type="run")
    depends_on("py-pysolar", type="run")
    depends_on("py-pyyaml@6:", type="run")
    depends_on("py-requests", type="run")
    depends_on("py-rich", type="run")
    depends_on("py-ruamel-yaml", type="run")
    depends_on("py-scikit-learn", type="run")
    depends_on("py-scipy", type="run")
    #depends_on("py-setuptools", type="run")
    depends_on("py-tables", type="run")
    depends_on("py-tol-colors", type="run")
    depends_on("py-tqdm", type="run")
    depends_on("py-typhon", type="run")
    depends_on("py-urllib3", type="run")
    #depends_on("py-wheel", type="run")
    depends_on("py-xarray", type="run")
    depends_on("py-zarr", type="run")

    # TODO:
    # py-geoviews, py-hvplot, py-holoviews, py-emcpy

    # There is no need for install() since there is no code.
