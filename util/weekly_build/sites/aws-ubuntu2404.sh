#!/bin/bash

COMPILERS=${COMPILERS:-"oneapi gcc"}
TEMPLATES=${TEMPLATES:-"unified-dev"}

# module --force purge
# umask 0022

SPACK_STACK_URL=https://github.com/stiggy87/spack-stack.git
SPACK_STACK_BRANCH=feature/hdf5-weekly-build-testing

PADDED_LENGTH=0
KEEP_WEEKLY_BUILD_DIR=YES
REUSE_BUILD_CACHE=YES
SKIP_FETCH=YES

PACKAGES_TO_TEST="hdf5"
PACKAGES_TO_INSTALL="ewok-env global-workflow-env jedi-fv3-env"
FIND_CMD="find"
TEST_UFSWM=OFF
