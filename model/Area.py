from db_instance import db

class Area(db.Model):
    __tablename__ = db.metadata.tables['Area']

    cep = db.Column('cep',db.varchar(8),nullable=False)