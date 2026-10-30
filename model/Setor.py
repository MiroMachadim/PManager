from db_instance import db

class Setor(db.Model):
    __table__ = db.metadata.tables['setor']