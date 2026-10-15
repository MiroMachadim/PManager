from db_instance import db
from model.Cargo import  Cargo

def enviarCargo(nome, pos):
    cargo = Cargo()
    cargo.c.nome = nome
    cargo.posicao = pos
    db.session.add(cargo)

    return db.session.commit()