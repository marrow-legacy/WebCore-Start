# encoding: utf-8

import web

from web.extras.quickstart import model

from web.extras.quickstart.controllers.metadata import MetadataController


__all__ = ['RootController']
log = __import__('logging').getLogger(__name__)



class RootController(web.core.Controller):
    # Overview Sub-Items
    metadata = MetadataController()
    
    def index(self):
        return 'web.extras.quickstart.templates.index', dict()
