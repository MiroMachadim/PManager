from db_instance import db


class Acesso(db.Model):
    __table__= db.metadata.tables['acesso_setor']
