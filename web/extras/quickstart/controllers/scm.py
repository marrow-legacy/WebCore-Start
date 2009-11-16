# encoding: utf-8

import web

from web.extras.quickstart import model


__all__ = ['SCMController']
log = __import__('logging').getLogger(__name__)



class SCMController(web.core.Controller):
    def index(self):
        return 'web.extras.quickstart.templates.scm', dict()
