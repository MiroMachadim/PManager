from db_instance import db
from model.Estado import Estado


class Bo(db.Model):
    __table__ = db.metadata.tables['bo']

    @property
    def tipo_crime(self):
        return db.session.scalar(
            db.select(Bo.nome).where(Bo.id == self.tipo_id)
        )

    @property
    def status(self):
        return db.session.scalar(
            db.select(Bo.nome).where(Estado.id == self.status_id)
        )


