from flask_login import UserMixin
from db_instance import db

class Cargo(UserMixin,db.Model):
    __tablename__ = 'cargo'

    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String)
    posicao = db.Column(db.Integer)
