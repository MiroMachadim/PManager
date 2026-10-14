from db_instance import db
from model.Policial import Policial


class Falta(db.Model):
    __tablename__ = db.metadata.tables['Falta']

    policial_id = db.Column('policial_id', db.Integer, db.ForeignKey(Policial.id))
    data_envio = db.Column('data_envio', db.Timestamp)
    data_fim = db.Column('data_fim', db.Date,nullable=True)
    justificativa = db.Column('justificativa',db.Text, nullable=True)