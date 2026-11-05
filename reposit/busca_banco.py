import model
from db_instance import db
from model.Ocorrencia import Bo
from model.Ficha import Ficha
from sqlalchemy import or_


def listar_oficiais() -> list:
    from model.Policial import Policial
    stmt = db.select(Policial)
    return db.session.execute(stmt).all()


def buscar_oficial(id: int):
    from model.Policial import Policial
    return db.session.get(Policial, id)


def buscar(tabela:db.Model,filtro) -> list:
    stmt = db.select(tabela).where(filtro)
    return db.session.execute(stmt).all()

def listar_tipo():
    from model.Tipo import Tipo
    stmt = db.select(Tipo)
    return db.session.execute(stmt).all()

def listar_Estado():
    from model.Estado import Estado
    stmt = db.select(Estado)

def OcorrenciaFicha(cpf):
    ocorrencias = db.session.scalars(
        db.select(Bo)
        .outerjoin(Ficha, Ficha.bo_id == Bo.id)
        .where(or_(Bo.cpf_vitima == cpf, Ficha.cpf == cpf))
        .order_by(Bo.created_at.desc())
    ).all()
    return ocorrencias

def executar_join(stmt) -> list | None:
    return db.session.execute(stmt).all()

def id_por_nome(tabela:db.Model, nome):
    if not nome:
        return None
    stmt = db.select(tabela.id).where(tabela.nome == nome)
    return db.session.scalar(stmt)

def area_por_nome(cep):
    if not cep:
        return None
    area = model.Area.Area
    stmt = db.select(area.id).where(area.cep == cep)
    return db.session.scalar(stmt)