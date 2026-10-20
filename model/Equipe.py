from db_instance import db


class Equipe(db.Model):
    __table__ = db.metadata.tables['Equipe']
