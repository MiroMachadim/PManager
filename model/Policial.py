from functools import wraps
from model.Cargo import Cargo
from db_instance import db
from flask_login import UserMixin, login_required
from ext import login_manager
from model.Pessoa import Pessoa
from reposit.conexao_banco import instanciar
from flask import redirect, url_for, flash
from flask_login import current_user
from model.Zona import Zona


class Policial(UserMixin,db.Model):
    __table__ = db.metadata.tables['policial']

    @property
    def pessoa(self):
        return instanciar(Pessoa, self.cpf)

    @property
    def nome_completo(self):
        return self.pessoa.nome if self.pessoa else None

    @property
    def data_nascimento(self):
        return self.pessoa.data_nascimento if self.pessoa else None

    @property
    def sexo(self):
        return self.pessoa.sexo if self.pessoa else None

    @property
    def cargo(self):
        c = db.session.get(Cargo, self.cargo_id) if self.cargo_id else None
        return c.nome if c else None


def get_id(self):
    return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    if not user_id:
        return None
    try:
        id_int = int(user_id)
        return db.session.get(Policial, id_int)
    except (ValueError, TypeError):
        return None

def admin_required(f):
    @wraps(f)
    @login_required
    def funcao(*args, **kwargs):
        if not current_user.admin:
            flash("Acesso restrito a administradores", "error")
            return redirect(url_for("hub.homepage"))
        return f(*args, **kwargs)
    return funcao