from datetime import date, datetime

from sqlalchemy import Date,select
from sqlalchemy.exc import InvalidRequestError
from db_instance import db
from service.chain import chain


def instanciar(tabela, chave):
    return db.session.get(tabela, chave)


def enviar() -> bool:
    try:
        db.session.commit()
        return True
    except Exception as e:
        print(f"erro ao enviar: {e}")
        db.session.rollback()
        return False


def selecionar_por_id(tabela, chave):
    stmt = db.select(tabela).where(tabela.id == chave)
    return db.session.scalar(stmt)


def listar(tabela) -> list:
    stmt = db.select(tabela)
    return db.session.scalars(stmt).all()


def listar_por_cpf(tabela, chave) -> list:
    stmt = db.select(tabela).where(tabela.cpf == chave)
    return db.session.scalars(stmt).all()


def selecionar_por_cpf(tabela, chave):
    stmt = db.select(tabela).where(tabela.cpf == chave)
    return db.session.scalar(stmt)


def selecionar_por_data(tabela, chave: date | datetime) -> list:
    stmt = (
        db.select(tabela)
        .where(tabela.created_at == chave)
        .order_by(tabela.id)
    )
    return db.session.scalars(stmt).all()


def inserir_dados(alvo, dados: dict, total: int) -> bool:
    if isinstance(alvo, type):
        instancia = alvo()
    else:
        instancia = alvo

    resultado = chain.handle(instancia, dados, total)

    if resultado is not None:
        print(f"Erro na cadeia de handlers: {resultado}")
        return False

    db.session.add(instancia)
    if enviar():
        return getattr(instancia, "id", True)
    else:
        return False