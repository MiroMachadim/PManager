from db_instance import db
class Cargo(db.Model):
    __tablename__ = db.metadata.tables['Cargo']

    posicao = db.Column("posicao", db.Integer, nullable=False)