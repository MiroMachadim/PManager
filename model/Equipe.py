from db_instance import db
from model.Policial import Policial
from model.Zona import Zona


class Equipe(db.Model):
    __tablename__ = db.metadata.tables['Equipe']

    id = db.Column("id",db.Integer, primary_key=True)
    zona_id = db.Column("zona_id", db.Integer, db.ForeignKey(Zona.id))
    lider_id = db.Column("lider_id", db.Integer, db.ForeignKey(Policial.id))