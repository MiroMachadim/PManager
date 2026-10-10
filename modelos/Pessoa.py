from flask_login import UserMixin

from db_instance import db

class Pessoa(UserMixin, db.Model):

    __tablename__ = 'pessoa'
    cpf = db.Collumn(db.String(11),primary_key=True)
    nome = db.Collumn(db.String(50),nullable=False)
    sexo = db.Collumn(db.char(1),nullable=False)
    idade = db.Collumn(db.Integer,nullable=False)