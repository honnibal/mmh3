# MurmurHash3 was written by Austin Appleby, and is placed in the public domain.
# mmh3 Python module was written by Hajime Senuma, and is also placed in the public domain.
# The authors hereby disclaim copyright to these source codes.
import sys
from setuptools import setup, Extension

COMPILE_OPTIONS = []
LINK_OPTIONS = []


def is_new_osx():
    """Check whether we're on OSX >= 10.10"""
    import distutils.util
    name = distutils.util.get_platform()
    if sys.platform != 'darwin':
        return False
    elif name.startswith('macosx-10'):
        minor_version = int(name.split('-')[1].split('.')[1])
        if minor_version >= 7:
            return True
        else:
            return False
    else:
        return False

if is_new_osx():
    # On Mac, use libc++ because Apple deprecated use of
    # libstdc
    COMPILE_OPTIONS.append("-stdlib=libc++")
    LINK_OPTIONS.append("-lc++")
    # g++ (used by unix compiler on mac) links to libstdc++ as a default lib.
    # See: https://stackoverflow.com/questions/1653047/avoid-linking-to-libstdc
    LINK_OPTIONS.append("-nodefaultlibs")

mmh3module = Extension('mmh3',
    sources = ['mmh3module.cpp', 'MurmurHash3.cpp'],
    extra_compile_args=COMPILE_OPTIONS,
    extra_link_args=LINK_OPTIONS)

setup(name = 'mmh3',
    version = '2.5.1',
    description = 'Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.',
    license = 'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    author = 'Hajime Senuma',
    author_email = 'hajime.senuma@gmail.com',
    url = 'http://packages.python.org/mmh3',
    ext_modules = [mmh3module],
    keywords = "utility hash MurmurHash",
    long_description = open('README.rst').read(),
    classifiers = ['Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities']
)
