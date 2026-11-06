from db_instance import db


class Falta(db.Model):
    __table__ = db.metadata.tables['falta']
