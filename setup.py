from setuptools import setup, find_packages

version = "1.2.0"

with open("./README.md") as fd:
    long_description = fd.read()

setup(
    name="pystripe",
    version=version,
    description=
    "Stripe artifact filtering for SPIM images",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy==1.24.2",
        "scipy==1.9.1",
        "scikit-image==0.20.0",
        "tifffile==2023.3.21",
        "PyWavelets==1.4.1",
        "tqdm==4.65.0",
        "pathlib2==2.3.7.post1",
        "dcimg==0.6.0.post1"
    ],
    author="LifeCanvas Technologies",
    packages=["pystripe"],
    entry_points={ 'console_scripts': [
        'pystripe=pystripe.core:main',
    ]},
    url="https://github.com/LifeCanvas-Technologies/pystripe",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 3.6',
    ]
)
