from db_instance import db
from flask_login import UserMixin


class Policial(UserMixin,db.Model):
    __table__ = db.metadata.tables['Policial']

