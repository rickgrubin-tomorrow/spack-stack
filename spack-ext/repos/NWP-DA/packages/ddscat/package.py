# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ddscat(MakefilePackage):
    """Discrete Dipole Scattering (DDSCAT) is a Fortran code for calculating scattering and absorption of light by irregular particles and periodic arrangement of irregular particles."""

    homepage = "http://ddscat.wikidot.com/"
    url = "http://ddscat.wikidot.com/local--files/downloads/ddscat7.3.3_220120.tgz"
    maintainers = ["rhoneyager-tomorrow"]

    version("7.3.3.220120", sha256="06f2673a45fcff20b8ed9f37d5bedeb84604d7a9fb10f627096833163769d1e7")

    depends_on("mpi")

    # precision=single precision=double
    # openmp
    # mkl
    # mpi


    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass
