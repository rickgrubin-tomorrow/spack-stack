#!/bin/bash

COMPILERS=${COMPILERS:-"gcc oneapi"}
TEMPLATES=${TEMPLATES:-"unified-dev"}

module --force purge
umask 0022

SPACK_STACK_URL=https://github.com/JCSDA/spack-stack.git
SPACK_STACK_BRANCH=feature/hdf5-weekly-build-testing

KEEP_WEEKLY_BUILD_DIR="NO"
PADDED_LENGTH=200

function alert_cmd {
  module purge # annoying libstdc++ issue
  mail -s 'spack-stack weekly build failure' sgrace@ucar.edu  < <(echo "Weekly spack-stack build failed in $1. Run ID: $RUNID")
}

PACKAGES_TO_TEST="hdf5 openmpi"
PACKAGES_TO_INSTALL="crtm esmf ewok-env global-workflow-env jedi-fv3-env gsi-env"
