"""A setuptools based setup module.
"""

from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.absolute()

# Get the long description from the README file
with open(here.joinpath('README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Add configuration files
extra_files = [str(here / 'pinar_petals/conf/pinar.conf')]

setup(
    name='pinar_petals',

    version='3.3.0',

    description='PINAR in Python',

    long_description=long_description,

    url='https://github.com/davidnbresch/pinar_python',

    author='ETH',

    license='OSI Approved :: GNU General Public License v3 (GPLv3)',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Topic :: Climate Adaptation',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='climate adaptation',

    packages=find_packages(where='.'),

    install_requires=[
        'pinar',
        'scikit-image',
    ],

    package_data={'': extra_files},

    include_package_data=True
)
