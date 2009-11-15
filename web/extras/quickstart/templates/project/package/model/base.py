# encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base


__all__ = ['Base']



class DeclarativeEntity(object):
    @classmethod
    def get(cls, *args, **kw):
        from coresite.model import session
        return session.query(cls).get(*args, **kw)


Base = declarative_base(cls=DeclarativeEntity)
