from db_instance import db
from model.Estado import Estado

def enviar_estado(nome):
    estado = Estado()
    estado.c.nome = nome
    db.session.add(estado)

    return db.session.commit()