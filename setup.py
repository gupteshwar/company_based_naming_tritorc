# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in company_based_naming/__init__.py
from company_based_naming import __version__ as version

setup(
	name='company_based_naming',
	version=version,
	description='Set naming of any doctype based on company ',
	author='First ERP',
	author_email='support@firsterp.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
