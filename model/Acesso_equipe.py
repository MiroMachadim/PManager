from db_instance import db

class Acesso_equipe(db.Model):
    __table__ = db.metadata.tables['acesso_equipe']

