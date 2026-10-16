from db_instance import db
from model.Area import Area
from model.Estado import Estado
from model.Pessoa import Pessoa
from model.Tipo import Tipo


class Bo(db.Model):
    __table__ = db.metadata.tables['Bo']

