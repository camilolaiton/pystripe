from sys import _version_info
from setuptools import setup, find_packages

exec(open('pystripe/version.py').read())

with open("./README.md") as fd:
    long_description = fd.read()

setup(
    name="pystripe",
    version=_version_info,
    description=
    "Stripe artifact filtering for SPIM images",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy",
        "scipy",
        "scikit-image",
        "tifffile",
        "PyWavelets",
        "tqdm",
        "pathlib2",
        "dcimg"
    ],
    author="Kwanghun Chung Lab",
    packages=["pystripe"],
    entry_points={ 'console_scripts': [
        'pystripe=pystripe.core:main',
    ]},
    url="https://github.com/joegruss/pystripe",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 3.6',
    ]
)
