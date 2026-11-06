from db_instance import db

class Tipo(db.Model):
    __table__ = db.metadata.tables['tipoocorrencia']
