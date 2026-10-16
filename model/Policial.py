from db_instance import db
from Cargo import Cargo
from model.Equipe import Equipe
from model.Pessoa import Pessoa
from flask_login import UserMixin


class Policial(UserMixin,db.Model):
    __table__ = db.metadata.tables['Policial']

