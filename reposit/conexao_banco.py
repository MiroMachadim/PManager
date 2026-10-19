from select import select
from sqlalchemy import Date
from db_instance import db


def instanciar(tabela: db.Model,chave):
    return db.session.get(tabela,chave)

def enviar(banco):
    return db.session.commit(banco)

def selecionar_por_id(tabela: db.Model,chave):
    stmt = select(tabela).where(tabela.c.id == chave)
    return db.session.execute(stmt).scalar()

def listar_por_cpf(tabela: db.Model,chave):
    stmt = select(tabela).where(tabela.c.cpf == chave)
    return db.session.scalars(stmt).all()

def listar(tabela: db.Model):
    return db.session.scalars(tabela).all()

def selecionar_por_cpf(tabela: db.Model,chave):
    stmt = select(tabela).where(tabela.c.cpf == chave)
    return db.session.scalars(stmt)

def selecionar_por_data(tabela: db.Model,chave: Date):
    stmt = select(tabela).where(tabela.c.created_at == chave).order_by(tabela.c.id)
    return db.session.scalars(stmt).all()