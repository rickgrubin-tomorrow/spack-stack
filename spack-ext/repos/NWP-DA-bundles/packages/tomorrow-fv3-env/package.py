# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack import *


class TomorrowFv3Env(BundlePackage):
    """Basic development environment used by other environments"""

    homepage = "https://github.com/jcsda/spack-stack"
    git      = "https://github.com/jcsda/spack-stack.git"

    maintainers = ['rhoneyager-tomorrow']

    version('0.0.1')

    depends_on('jedi-fv3-env', type='run')
    depends_on('tomorrow-base-env', type='run')

    # There is no need for install() since there is no code.

