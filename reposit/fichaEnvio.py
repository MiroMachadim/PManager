from db_instance import db
from model.Ficha import Ficha

def enviar_ficha(cpf,bo):
    ficha = Ficha()
    ficha.pessoa_cpf = cpf
    ficha.bo_id = bo

    db.session.add(ficha)
    return db.session.commit()