# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in g1victoria/__init__.py
from g1victoria import __version__ as version

setup(
	name='g1victoria',
	version=version,
	description='G1Victoria ERP',
	author='Vesper Solutions ',
	author_email='vespersolutionspk@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
