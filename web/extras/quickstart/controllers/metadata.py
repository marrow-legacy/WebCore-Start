# encoding: utf-8

import web

from web.extras.quickstart import model


__all__ = ['MetadataController']
log = __import__('logging').getLogger(__name__)



class MetadataController(web.core.Controller):
    def index(self):
        return 'web.extras.quickstart.templates.metadata', dict()
