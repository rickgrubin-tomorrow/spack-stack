# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import shutil
import sys


class Rttov(MakefilePackage):
    """
    RTTOV (Radiative Transfer for TOVS) is a very fast radiative transfer model for passive visible, infrared
    and microwave downward-viewing satellite radiometers, spectrometers and interferometers.
    """

    homepage = "https://nwp-saf.eumetsat.int/site/software/rttov/"
    git = "ssh://git@github.com/rhoneyager-tomorrow/rttov.git"
    url = "https://github.com/rhoneyager-tomorrow/rttov/archive/refs/tags/v12.0.0.tar.gz"

    maintainers = ['rhoneyager-tomorrow']

    version('12.0.0', commit='20a00da2560b3ddeb0ef3c8300f88a331cd1a4cd', preferred=True)
    build_directory = 'src'

    parallel = False

    variant('f2py', default=False, description='Create Python bindings')

    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('hdf5')
    depends_on('mpi')
    depends_on('py-numpy', when='+f2py') # f2py

# for hdf5, need to edit build/Makefile.local
# for netcdf, need to edit build/Makefile.local
# optional link against lapack by editing build/Makefile.local
# need to set INSTALLDIR

    def edit(self, spec, prefix):
        archconfig = [
            'FC = {0}'.format(spec['mpi'].mpifc),
            'FC77 = {0}'.format(spec['mpi'].mpif77),
            'CC = {0}'.format(spec['mpi'].mpicc),
#            'LDFLAGS_ARCH=',
#            'CFLAGS_ARCH=',
#            'AR=ar r',
#            'FFLAGS_ARCH=',
#            '#FFLAGS_ARCH_rttov_add_aux_prof=',
#            '#FFLAGS_ARCH_rttov_dom_setup_profile_tl=',
#            'FFLAGS_ARCH_rttov_dom_setup_profile=',
#            'F2PY=f2py --fcompiler=pg',
            'F2PYFLAGS_ARCH=\"-fPIC\"',
#            'F2PYLDFLAGS_ARCH=',
        ]
        if '+f2py' in spec:
            archconfig.append('F2PY=f2py')
        if 'gfortran' in self.compiler.fc:
            archconfig.append('FFLAGS_ARCH=-fPIC -O3 -ffree-line-length-none')
            archconfig.append('LDFLAGS_ARCH=-shared')
            archconfig.append('FFLAGS_ARCH_lapack=-fPIC -O3')
        if 'ifort' in self.compiler.fc:
            archconfig.append('FFLAGS_ARCH=-fPIC -O3 -fp-model source')
        if 'gcc' in self.compiler.cc:
            archconfig.append('CFLAGS_ARCH=-fPIC')

        with open('src/build/arch/custom', 'w') as inc:
            for var in archconfig:
                inc.write('{0}\n'.format(var))

        makefilelocalconfig = [
            'HDF5_PREFIX = /{0}'.format(spec['hdf5'].prefix), # Somehow, format(...) is missing the leading '/'
            'FFLAGS_HDF5  = -D_RTTOV_HDF $(FFLAG_MOD)$(HDF5_PREFIX)/include',
            'LDFLAGS_HDF5 = -L$(HDF5_PREFIX)/lib -lhdf5_hl_fortran -lhdf5_hl -lhdf5_fortran -lhdf5 -lz -ldl',
            'NETCDF_PREFIX  = /{0}'.format(spec['netcdf-fortran'].prefix),
            'FFLAGS_NETCDF  = -D_RTTOV_NETCDF -I$(NETCDF_PREFIX)/include',
            'LDFLAGS_NETCDF = -L$(NETCDF_PREFIX)/lib -lnetcdff',
            'FFLAGS_EXTERN  = $(FFLAGS_NETCDF)  $(FFLAGS_HDF5)',
            'LDFLAGS_EXTERN = $(LDFLAGS_NETCDF) $(LDFLAGS_HDF5)',
        ]

        with open('src/build/Makefile.local', 'w') as inc:
            for var in makefilelocalconfig:
                inc.write('{0}\n'.format(var))

        #if sys.platform == 'darwin':
        #    env['ARCH'] = 'gfortran'
        env['ARCH'] = 'custom'
        env['INSTALLDIR'] = self.stage.source_path  # self.stage.source_path

    def install(self, spec, prefix):
        """Copies bin, include, lib, and mod directories to the install location.
        """
        shutil.copytree(self.stage.source_path + '/bin', prefix + '/bin')
        shutil.copytree(self.stage.source_path + '/include', prefix + '/include')
        shutil.copytree(self.stage.source_path + '/lib', prefix + '/lib')
        shutil.copytree(self.stage.source_path + '/mod', prefix + '/mod')

