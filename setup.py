
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='plotnine-prism',
    version='0.0.0',
    description='Prism themes for plotnine, inspired by ggprism',
    python_requires='==3.*,>=3.7.0',
    author='pwwang',
    author_email='pwwang@pwwang.com',
    license='GNU General Public License v2.0',
    packages=['plotnine_prism'],
    package_dir={"": "."},
    package_data={"plotnine_prism": ["schemes/*.toml"]},
    install_requires=['diot==0.*,>=0.1.1', 'plotnine==0.*,>=0.8.0', 'toml==0.*,>=0.10.2'],
)
