from setuptools import setup, Extension

# HDF5 settings
HDF5_ON = True
libraries = []
macros = []

# Check for h5cc
import distutils.spawn
h5cc_executable = distutils.spawn.find_executable('h5cc')
h5cc_present = not (h5cc_executable == None)

# if h5cc_present and HDF5_ON:
#     libraries.append('hdf5')
#     macros.append(('CUTOUT_SUPPORT', '1'))

libJHTDB = Extension(
    'libJHTDB',
    sources = [
        'C/local_tools.c',
        'turblib/turblib.c',
        'turblib/soapC.c',
        'turblib/soapClient.c',
        'turblib/stdsoap2.c'
    ],
    include_dirs = ['turblib'],
    define_macros = macros,
    libraries = libraries
)

setup(
    ext_modules = [libJHTDB],
)