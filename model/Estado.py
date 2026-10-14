from db_instance import db

class Estado(db.Model):
    __tablename__ = db.metadata.tables['Estados']

    id = db.Column("id", db.Integer, primary_key=True)