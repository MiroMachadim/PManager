from db_instance import db

class Tipo(db.Model):
    __tablename__ = db.metadata.tables['TipoOcorrencia']

    id = db.Column("id", db.Integer, primary_key=True)