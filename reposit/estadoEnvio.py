from db_instance import db
from model.Estado import Estado

def enviarEstado(nome):
    estado = Estado()
    estado.c.nome = nome
    db.session.add(estado)

    return db.session.commit()