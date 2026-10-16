from db_instance import db
from model.Tipo import Tipo

def enviar_tipo(nome):
    tipo = Tipo()
    tipo.c.nome = nome

    db.session.add(tipo)

    return db.session.commit()