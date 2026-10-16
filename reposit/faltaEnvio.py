from db_instance import db
from model.Falta import Falta
from datetime import datetime, timezone



def enviar_falta(policial,justificativa, data_fim):
    falta = Falta()
    falta.c.policial_id = policial
    falta.c.data_envio = datetime.now(timezone.utc)
    falta.c.data_fim = data_fim
    falta.c.justificativa = justificativa
    falta.c.data_fim = data_fim

    db.session.add(falta)
    return db.session.commit()