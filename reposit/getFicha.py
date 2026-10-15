from select import select
from db_instance import db
from model.Ficha import Ficha

def getFicha(cpf):
    ficha = Ficha()
    stmt = select(ficha).where(ficha.pessoa_cpf == cpf)
    result = db.session.execute(stmt).fetchall()
    return result