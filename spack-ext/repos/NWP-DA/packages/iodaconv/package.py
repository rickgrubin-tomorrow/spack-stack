# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Iodaconv(CMakePackage):
    """Converters for data to JEDI."""

    homepage = "https://www.jcsda.org/jcsda-project-jedi"
    git = 'https://github.com/JCSDA-internal/ioda-converters.git'

    maintainers = ["rhoneyager-tomorrow"]

    depends_on('bufr@12.0.1:')
    depends_on('ecbuild', type=('build'))
    depends_on('eccodes')
    depends_on('eckit')
    depends_on('eigen')
    depends_on('fckit')
    depends_on('gsl-lite')
    depends_on('hdf5')
    depends_on('ioda@2.9:')
    depends_on('jedi-cmake', type=('build'))
    depends_on('mpi')
    depends_on('netcdf-fortran')
    depends_on('oops')
    depends_on('python@3.7:')
    depends_on('py-pybind11')

    # Upstream versions with buggy installation instructions.
    #version('0.0.1.2024.09.06', commit='95deb2c468e8e687b566623582eafdf31e337a71') # Close to SkyLab 9
    version('0.0.1.2024.04.02', commit='0bc00802515fe5834fb70311bfcac3f4cf12d349') # SkyLab 8
    patch('cmake-2024.04.02.patch', when='@0.0.1.2024.04.02')

