from db_instance import db
from model.Policial import Policial


class Falta(db.Model):
    __table__ = db.metadata.tables['Falta']
