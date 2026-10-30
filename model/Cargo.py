from db_instance import db
class Cargo(db.Model):
    __table__ = db.metadata.tables['cargo']
