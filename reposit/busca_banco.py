import reposit.conexao_banco as cb
from model.Policial import Policial
from sqlalchemy import select
from db_instance import db


def listar_oficiais() -> list:
    oficiais = cb.listar(Policial)
    return oficiais

def buscar_oficial(id):
    return cb.selecionar_por_id(Policial, id)

def buscar(tabela:db.Model,stmt):
    return db.session.scalars(select(tabela).where(stmt)).all()

def join_ficha(stmt):
    return db.session.scalar(stmt).all()
