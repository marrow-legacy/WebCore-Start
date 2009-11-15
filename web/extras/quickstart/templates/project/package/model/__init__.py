# encoding: utf-8

from paste.registry import StackedObjectProxy

from ${package.name}.model.base import *
{% for db in app.development.db %}
from ${package.name}.model.${db.name} import *
{% end %}


metadata = Base.metadata
session = StackedObjectProxy()



def prepare():
    metadata.create_all()


def populate(session, table):
    pass
