from db_instance import db
from flask_login import UserMixin
from ext import login_manager
from model.Pessoa import Pessoa
from reposit.conexao_banco import instanciar


class Policial(UserMixin,db.Model):
    __table__ = db.metadata.tables['policial']

def get_id(self):
    return str(self.id)

@property
def nome(self):
   p = instanciar(Pessoa,self.cpf)
   return p.nome if p else None

@login_manager.user_loader
def load_user(user_id):
    if not user_id:
        return None
    try:
        id_int = int(user_id)
        return db.session.get(Policial, id_int)
    except (ValueError, TypeError):
        return None
