from db_instance import db
from model.Estado import Estado
from model.Tipo import Tipo


class Bo(db.Model):
    __table__ = db.metadata.tables['bo']

    @property
    def tipo_crime(self):
        return db.session.scalar(
            db.select(Tipo.nome).where(Tipo.id == self.tipo_id)
        )

    @property
    def status(self):
        return db.session.scalar(
            db.select(Estado.nome).where(Estado.id == self.estado_id)
        )

    @property
    def data_registro(self):
        return self.created_at


    @property
    def policial_responsavel(self):
        from model.Policial import Policial
        from model.Pessoa import Pessoa
        return db.session.scalar(
            db.select(Pessoa.nome)
            .join(Policial, Policial.cpf == Pessoa.cpf)
            .where(Policial.id == self.created_by)
        )


    @property
    def policial_editor(self):
        if self.updated_by is None:
            return None
        from model.Policial import Policial
        from model.Pessoa import Pessoa
        return db.session.scalar(
            db.select(Pessoa.nome)
            .join(Policial, Policial.cpf == Pessoa.cpf)
            .where(Policial.id == self.updated_by)
        )


