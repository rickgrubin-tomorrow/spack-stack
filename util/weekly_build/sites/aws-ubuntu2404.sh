#!/bin/bash

COMPILERS=${COMPILERS:-"gcc oneapi"}
TEMPLATES=${TEMPLATES:-"unified-dev"}

# module --force purge
# umask 0022

source /opt/intel/oneapi/setvars.sh --force

SPACK_STACK_URL=https://github.com/stiggy87/spack-stack.git
SPACK_STACK_BRANCH=feature/hdf5-weekly-build-testing

KEEP_WEEKLY_BUILD_DIR="NO"

PACKAGES_TO_TEST="hdf5"
PACKAGES_TO_INSTALL="ewok-env global-workflow-env jedi-fv3-env"
FIND_CMD="find"
TEST_UFSWM=OFF
KEEP_WEEKLY_BUILD_DIR="YES"