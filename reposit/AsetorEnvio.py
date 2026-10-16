from db_instance import db
from model.Acesso_Setor import Acesso


def envio_setor(policial,setor):

    acesso = Acesso()

    verificarDuplicado(policial,setor)

    acesso.c.setor_id = setor
    acesso.c.policial_id = policial

    db.session.add(acesso)
    return db.session.commit()

def verificar_duplicado(policial,setor):
    acesso = Acesso()
    dupli = db.session.execute(db.select(acesso).where(acesso.c.policial_id==policial,acesso.c.setor_id == setor))
    if dupli.length() > 0:
        raise Exception("ja colocado")

