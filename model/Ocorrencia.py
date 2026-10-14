from db_instance import db
from model.Area import Area
from model.Estado import Estado
from model.Pessoa import Pessoa
from model.Tipo import Tipo


class Bo(db.Model):
    __tablename__ = db.metadata.tables['Bo']

    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.Date, nullable=False)
    updated_at = db.Column("updated_at", db.Date, nullable=False)
    created_by = db.Column("created_by", db.varchar(8), db.ForeignKey(Pessoa.cpf), nullable=False)
    updated_by = db.Column("updated_by", db.varchar(8), db.ForeignKey(Pessoa.cpf), nullable=False)
    tipo_bo = db.Column("tipo_id", db.Integer , db.ForeignKey(Tipo.id))
    conteudo = db.Column("conteudo", db.Text, nullable=False)
    localidade = db.Column("localidade", db.Integer, db.ForeignKey(Area.id))
    estado = db.Column("estado", db.Integer, db.ForeignKey(Estado.id))
