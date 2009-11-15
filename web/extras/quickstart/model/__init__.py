# encoding: utf-8

from web.utils.dictionary import adict

__all__ = []



class Project(adict):
    def __init__(self):
        super(Project, self).__init__()
        
        self.update(dict(
                name = None,
                version = None,
                description = None,
                long_description = None,
                author = None,
                author_email = None,
                maintainer = None,
                maintainer_email = None,
                url = None,
                download_url = None,
                classifiers = [],
                license = None,
                keywords = [],
                include_package_data = True,
                zip_safe = False,
                install_requires = ['YAPWF'],
                test_suite = 'nose.collector',
                tests_require = ['nose', 'coverage'],
            ))



