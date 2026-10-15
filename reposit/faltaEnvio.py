from db_instance import db
from model.Falta import Falta
from datetime import datetime, timezone

def enviarFalta(policial,justificativa):
    falta = Falta()
    falta.policial_id = policial
    falta.data_envio = datetime.now(timezone.utc)
    falta.justificativa = justificativa

    db.session.add(falta)
    return db.session.commit()