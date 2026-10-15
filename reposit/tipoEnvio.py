from db_instance import db
from model.Tipo import Tipo

def enviarTipo(nome):
    tipo = Tipo()
    tipo.c.nome = nome

    db.session.add(tipo)

    return db.session.commit()