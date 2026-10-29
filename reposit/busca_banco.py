import reposit.conexao_banco as cb
import model
from db_instance import db


def listar_oficiais() -> list:
    oficiais = cb.listar(model.Policial.Policial())
    return oficiais

def buscar_oficial(id):
    return cb.selecionar_por_id(model.Policial.Policial(), id)

def buscar(tabela:db.Model,stmt):
    return db.session.scalars(db.session.select(tabela).where(stmt)).all()

def join_ficha(stmt):
    return db.session.scalars(stmt).all()
