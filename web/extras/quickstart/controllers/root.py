# encoding: utf-8

import web

from web.extras.quickstart import model

from web.extras.quickstart.controllers.metadata import MetadataController
from web.extras.quickstart.controllers.scm import SCMController


__all__ = ['RootController']
log = __import__('logging').getLogger(__name__)



class RootController(web.core.Controller):
    # Overview Sub-Items
    metadata = MetadataController()
    scm = SCMController()
    
    def index(self):
        return 'web.extras.quickstart.templates.index', dict()
