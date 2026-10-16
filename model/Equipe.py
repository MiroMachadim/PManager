from db_instance import db
from model.Policial import Policial
from model.Zona import Zona


class Equipe(db.Model):
    __table__ = db.metadata.tables['Equipe']
