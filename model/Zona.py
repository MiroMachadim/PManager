from db_instance import db
from model.Area import Area


class Zona(db.Model):
    __table__ = db.metadata.tables['Zona']
