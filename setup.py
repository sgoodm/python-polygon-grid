import os
import sys
import re
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    vfile = os.path.join(
        os.path.dirname(__file__), "src", "polygongrid", "_version.py")
    with open(vfile, "r") as vfh:
        vline = vfh.read()
    vregex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    match = re.search(vregex, vline, re.M)
    if match:
        return match.group(1)
    else:
        raise RuntimeError("Unable to find version string in {}.".format(vfile))

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="polygongrid",
    version=get_version(),
    author="Seth Goodman",
    author_email="sgoodman@aiddata.wm.edu",
    description="Generate polygon grids",
    license="BSD",
    keywords="gis geospatial geographic vector grid",
    url="https://github.com/sgoodm/python-polygon-grid",
    package_dir={'': 'src'},
    packages=['polygongrid'],
    long_description=read('README.md'),
    install_requires=read('requirements.txt').splitlines(),
    tests_require=['pytest', 'pytest-cov>=2.2.0', 'coverage'],
    cmdclass={'test': PyTest},
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Topic :: Utilities",
        'Topic :: Scientific/Engineering :: GIS',
    ]
)
