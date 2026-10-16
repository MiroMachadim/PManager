from db_instance import db
from model.Equipe import Equipe

def enviar_equipe(zona,lider):
    equipe = Equipe()
    equipe.c.zona_id = zona
    equipe.c.lider_id = lider

    db.session.add(equipe)
    return db.session.commit()

def trocar_lider(id,lider):
    equipe = db.session.get(Equipe, id)
    equipe.c.lider_id = lider
    db.session.commit()
