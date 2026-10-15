from db_instance import db
from model.Equipe import Equipe

def enviarEquipe(zona,lider):
    equipe = Equipe()
    equipe.zona_id = zona
    equipe.lider_id = lider

    db.session.add(equipe)
    return db.session.commit()
