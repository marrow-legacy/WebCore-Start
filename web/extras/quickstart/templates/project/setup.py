#!/usr/bin/env python
# encoding: utf-8

import sys, os

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

if sys.version_info <= (2, 5):
    raise SystemExit("Python 2.5 or later is required.")

execfile(os.path.join("${package.name}", "release.py"))


setup(
        name = name,
        version = version,
        
        description = summary,
        long_description = description,
        author = author,
        author_email = email,
        url = url,
        download_url = download_url,
        license = license,
        keywords = '',
        
        install_requires = [
                'WebCore',
{% for pkg in app.requirements %}
                '${pkg}',
{% end %}
            ],
        
        test_suite = 'nose.collector',
        tests_require = ['nose', 'coverage'],
        
        classifiers = [
{% for classifier in app.classifiers %}
                "${classifier}",
{% end %}
            ],
        
        packages = find_packages(exclude=['docs', 'tests', 'tests.*']),
        include_package_data = True,
        zip_safe = False
    )
