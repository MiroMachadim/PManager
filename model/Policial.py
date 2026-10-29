from sqlalchemy.testing.pickleable import User
from db_instance import db
from flask_login import UserMixin

from ext import login_manager


class Policial(UserMixin,db.Model):
    __table__ = db.metadata.tables['Policial']

    @login_manager.user_loader
    def load_user(user_id):
        return Policial.query.get(int(user_id))