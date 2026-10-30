from db_instance import db

class Area(db.Model):
    __table__ = db.metadata.tables['area']
