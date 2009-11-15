#!/usr/bin/env python
# encoding: utf-8

import sys, os

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages


if sys.version_info <= (2, 5):
    raise SystemExit("Python 2.5 or later is required.")

execfile(os.path.join("web", "extras", "quickstart", "release.py"))



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
                'Beaker',
                'Genshi',
                'Unipath',
            ],
        
        test_suite = 'nose.collector',
        tests_require = [
                'nose',
                'coverage'
            ],
        
        classifiers = [
                "Development Status :: 1 - Planning",
                "Environment :: Console",
                "Framework :: Paste",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Programming Language :: Python",
                "Topic :: Internet :: WWW/HTTP :: WSGI",
                "Topic :: Software Development :: Libraries :: Python Modules"
            ],
        
        packages = find_packages(exclude=['ez_setup', 'examples', 'tests', 'tests.*', 'docs']),
        include_package_data = True,
        zip_safe = False,
        
        namespace_packages = [
                'web',
                'web.extras',
            ],
        
        entry_points = {
                'paste.paster_command': [
                        'quickstart = web.commands.quickstart:StartCommand'
                    ],
            }
    )
