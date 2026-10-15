from db_instance import db
from Cargo import Cargo
from model.Equipe import Equipe
from model.Pessoa import Pessoa
from flask_login import UserMixin


class Policial(UserMixin,db.Model):
    __tablename__ = db.metadata.tables['Policial']

    id = db.Column("id", db.Integer, primary_key=True)
    cpf = db.Column("cpf", db.Integer, db.ForeignKey(Pessoa.cpf))
    senha = db.Column("id", db.UUID, primary_key=True)
    cargo_id = db.Column("cargo_id",db.Integer, db.ForeignKey(Cargo.c.id))
