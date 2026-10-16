from db_instance import db
from model.Zona import Zona

def enviar_zona(nome,area):
    zona = Zona()
    zona.nome = nome
    zona.area_id = area

    db.session.add(zona)
    db.session.commit()

def trocar_nome(id,nome):
    zona = db.session.get(Zona,id)
    zona.c.nome = nome
    return db.session.commit()