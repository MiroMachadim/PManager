from db_instance import db
from model.Policial import Policial
from model.Setor import Setor


class Acesso(db.Model):
    __table__= db.metadata.tables['Acesso_setor']
