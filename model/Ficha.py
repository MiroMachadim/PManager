from db_instance import db
from model.Pessoa import Pessoa
from model.Ocorrencia import Bo


class Ficha(db.Model):
    __tablename__ = db.metadata.tables['Ficha']

    id = db.Column('id',db.Integer, primary_key=True)
    pessoa_cpf = db.Column('pessoa_cpf', db.varchar(11), db.ForeignKey(Pessoa.cpf))
    bo_id = db.Column("bo_pessoa", db.Integer, db.ForeignKey(Bo.id))