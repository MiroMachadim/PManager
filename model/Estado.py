from db_instance import db

class Estado(db.Model):
    __table__ = db.metadata.tables['Estados']
