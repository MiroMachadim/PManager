from db_instance import db


class Ficha(db.Model):
    __table__ = db.metadata.tables['Ficha']
