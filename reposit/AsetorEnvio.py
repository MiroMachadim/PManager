from db_instance import db
from model.Acesso_Setor import Acesso


def envioSetor(policial,setor):

    acesso = Acesso()

    verificarDuplicado(policial,setor)

    acesso.setor_id = setor
    acesso.policial_id = policial

    db.session.add(acesso)
    return db.session.commit()

def verificarDuplicado(policial,setor):
    acesso = Acesso()
    dupli = db.session.execute(db.select(acesso).where(acesso.policial_id==policial,acesso.setor_id == setor))
    if dupli.length() > 0:
        raise Exception("ja colocado")

