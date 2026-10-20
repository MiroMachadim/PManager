from select import select
from sqlalchemy import Date
from db_instance import db
from service.chain import chain


def instanciar(tabela: db.Model,chave):
    return db.session.get(tabela,chave)

def enviar(tabela: db.Model):
    return db.session.commit(tabela)

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

def inserir_dados(tabela: db.Model, dados, total ):
    chain.handle(tabela, dados, total)
    return enviar(tabela)
