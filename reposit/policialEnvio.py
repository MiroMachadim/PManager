from db_instance import db
from model.Policial import Policial

def enviarPolicial(cpf, senha, cargo):
    policial = Policial()
    policial.cpf = cpf
    policial.senha = senha
    policial.cargo = cargo

    db.session.add(policial)
    return db.session.commit()