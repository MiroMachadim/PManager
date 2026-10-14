from db_instance import db

class Pessoa(db.Model):
    __tablename__ = db.metadata.tables['Pessoa']

    cpf = db.Column("cpf", db.String(11), primary_key=True)
    nome = db.Column("nome", db.String(100), nullable=False)