from db_instance import db

class Pessoa(db.Model):
    __table__ = db.metadata.tables['pessoa']
