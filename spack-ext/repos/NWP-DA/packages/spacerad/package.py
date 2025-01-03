# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Spacerad(PythonPackage):
    """A collection of functions and algorithms for spaceborne radar observation simulation."""

    homepage = "https://github.com/climacell/spacerad"
    git = "git@github.com:climacell/spacerad.git"
    url = "https://github.com/climacell/spacerad/archive/refs/tags/0.0.1.tar.gz"

    maintainers = ['rhoneyager-tomorrow']

    version("0.0.1a", commit="6c7c4878ab92f7ed79073b46104cd2f61579ba92")

    depends_on("cmake@3.6:", type="build")
    depends_on("py-numpy", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("PyTMatrix", type="build")

