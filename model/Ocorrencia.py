from db_instance import db


class Bo(db.Model):
    __table__ = db.metadata.tables['bo']

