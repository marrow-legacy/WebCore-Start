# encoding: utf-8

import web
{% if app.authentication %}
from web.auth import authorize
{% end %}

{% if app.db %}
from ${package.name} import model as db
{% end %}


__all__ = ['RootController']
log = __import__('logging').getLogger(__name__)



class RootController(web.core.Controller):
    def index(self):
        return '${package.name}.templates.index', dict()
