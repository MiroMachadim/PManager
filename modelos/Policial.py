from flask_login import UserMixin
from db_instance import db
from modelos.Cargo import Cargo
from modelos.Pessoa import Pessoa


class Policial(UserMixin,db.Model):
    __tablename__ = 'policial'

    id = db.Column(db.Integer, primary_key=True)
    pessoa_cpf = db.Column(db.ForeignKey(Pessoa.cpf),nullable=False)
    cargo_id = db.Column(db.ForeignKey(Cargo.id),nullable=False)