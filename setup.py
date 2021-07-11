# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in g1fiba/__init__.py
from g1fiba import __version__ as version

setup(
	name='g1fiba',
	version=version,
	description='G1Fiba ERP',
	author='Vesper Solutions ',
	author_email='vespersolutionspk@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
