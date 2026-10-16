from db_instance import db
from model.Pessoa import Pessoa
from model.Ocorrencia import Bo


class Ficha(db.Model):
    __table__ = db.metadata.tables['Ficha']
