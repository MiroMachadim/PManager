from db_instance import db
from model.Policial import Policial
from model.Setor import Setor


class Acesso(db.Model):
    __tablename__ = db.metadata.tables['Acesso_setor']
    id = db.Column("id",db.Integer, primary_key=True)
    setor_id = db.Column("setor_id",db.Integer, db.ForeignKey(Setor.id))
    policial_id = db.Column("policial_id", db.Integer, db.ForeignKey(Policial.id))
