from db_instance import db
from model.Area import Area


class Zona(db.Model):
    __tablename__ = db.metadata.tables['Zona']

    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.varchar(50),unique=True, nullable=False)
    area_id = db.Column('area_id',db.Integer, db.ForeignKey(Area.id), nullable = False)