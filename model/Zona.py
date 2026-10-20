from db_instance import db


class Zona(db.Model):
    __table__ = db.metadata.tables['Zona']
