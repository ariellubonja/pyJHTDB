########################################################################
#
#  Copyright 2014 Johns Hopkins University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Contact: turbulence@pha.jhu.edu
# Website: http://turbulence.pha.jhu.edu/
#
########################################################################

"""
Python tools and wrappers for the Johns Hopkins Turbulence Database
Cluster C library.
Contact: turbulence@pha.jhu.edu
Website: http://turbulence.pha.jhu.edu/

Although this particular Python wrapper is still a work in progress, it
is mature enough to be used in production work.

On first contact with this library, we recommend that you first run
"test_plain". To be more specific:

.. code:: python

    >>> from pyJHTDB import test_plain
    >>> test_plain()

The code that is executed can be found in "pyJHTDB/test.py", and it's
the simplest example of how to access the turbulence database.

"""

# Import version first, before any dependencies
from ._version import __version__

# Now import standard library modules
import os
import os.path
import sys
import platform

# Import third-party dependencies
import numpy as np
import ctypes

# Rest of your initialization code
auth_token = 'edu.jhu.pha.turbulence.testing-201406'
homefolder = os.path.expanduser('~')
lib_folder = os.path.join(homefolder, '.config/', 'JHTDB/')

# check if .config/JHTDB folder exists, create it if not
#if os.path.isdir(lib_folder):
#    if os.path.exists(os.path.join(lib_folder, 'auth_token.txt')):
#        auth_token = str(open(os.path.join(lib_folder, 'auth_token.txt'), 'r').readline().split()[0])
#    else:
#        open(os.path.join(lib_folder, 'auth_token.txt'), 'w').write(auth_token)
#else:
#    os.mkdir(lib_folder)
#    open(os.path.join(lib_folder, 'auth_token.txt'), 'w').write(auth_token)

try:
    import h5py
    found_h5py = True
except ImportError:
    found_h5py = False
    print('h5py not found. cutout functionality not available.')

try:
    import matplotlib
    found_matplotlib = True
except ImportError:
    found_matplotlib = False
    print('matplotlib not found. plotting functionality not available.')

try:
    import scipy
    found_scipy = True
except ImportError:
    found_scipy = False
    print('scipy not found. not all interpolation functionality available')

from .libJHTDB import *
from .test import test_plain
if found_matplotlib:  # Fixed: was pyJHTDB.found_matplotlib
    from .test import test_misc
from .test import test_interp_1D as test_interpolator
from .generic_splines import main0 as test_gs