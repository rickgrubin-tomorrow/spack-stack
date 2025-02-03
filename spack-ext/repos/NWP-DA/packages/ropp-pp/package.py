# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RoppPp(AutotoolsPackage):
    """
    The Radio Occultation Processing Package (ROPP) is a package of software (as source code)
    and supporting build and test scripts, data files and documentation, which will aid users
    wishing to process, quality-control and assimilate radio occultation data from any radio
    occultation mission into NWP and other models.
    """

    homepage = "https://www.romsaf.org/ropp"
    git = "ssh://git@github.com/rhoneyager-tomorrow/ropp.git"
    url = "https://github.com/rhoneyager-tomorrow/ropp/archive/refs/tags/v10.0.0.tar.gz"

    maintainers = ['rhoneyager-tomorrow']

    version('10.0.0', commit='874cf5869ff4d928c2c030fea6ea53c9de5f050f', preferred=True)
    configure_directory = 'src/ropp_pp'
    parallel = False

    # See ROPP release notes. eccodes 2.22.0 support added in v11.
    depends_on('eccodes@:2.21.0', when='@:10.0.0')
    depends_on('eccodes', when='@11.0.0:')

    depends_on('hdf5')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')

    depends_on('ropp-utils')
    depends_on('ropp-io')

    # ROPP_ROOT must be set to the installation location.
    def setup_build_environment(self, env):
        env.prepend_path('ROPP_ROOT', self.prefix)
        env.append_flags('FFLAGS', self.compiler.fc_pic_flag)
        env.append_flags('FCFLAGS', self.compiler.fc_pic_flag)

    # BUFR_TABLES must be set at runtime for ROPP to find the BUFR tables
    def setup_run_environment(self, env):
        env.prepend_path('BUFR_TABLES', self.prefix + '/data/bufr')


