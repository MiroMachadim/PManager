from sqlalchemy import Date,select
from sqlalchemy.exc import InvalidRequestError
from db_instance import db
from service.chain import chain


def instanciar(tabela: db.Model,chave):
    return db.session.get(tabela,chave)

def enviar():
    try:
        return db.session.commit()
    except Exception:
        print("erro ao enviar")
        return db.session.rollback()

def selecionar_por_id(tabela: db.Model,chave):
    stmt = select(tabela).where(tabela.id == chave)
    return db.session.execute(stmt).scalar()

def listar_por_cpf(tabela: db.Model,chave):
    print(list(tabela.keys()))
    stmt = select(tabela).where(tabela.cpf == chave)
    return db.session.scalars(stmt).all()

def listar(tabela: db.Model):
    return db.session.scalars(tabela).all()

def selecionar_por_cpf(tabela: db.Model,chave):
    stmt = select(tabela).where(tabela.cpf == chave)
    try:
        linha = db.session.scalar(stmt)
    except (InvalidRequestError, Exception):
        return None
    return linha

def selecionar_por_data(tabela: db.Model,chave: Date):
    stmt = select(tabela).where(tabela.created_at == chave).order_by(tabela.id)
    return db.session.scalars(stmt).all()

def inserir_dados(tabela: db.Model, dados, total ):
    inserido = chain.handle(tabela, dados, total)
    return enviar()
