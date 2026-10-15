from db_instance import db
from model.Acesso_Setor import Acesso


def envioSetor(policial,setor):

    asetor = Acesso()

    verificarDuplicado(policial,setor)

    asetor.setor_id = setor
    asetor.policial_id = policial

    db.session.add(asetor)
    return db.session.commit()

def verificarDuplicado(policial,setor):
    asetor = Acesso()
    dupli = db.session.execute(db.select(asetor).where(asetor.policial_id==policial,asetor.setor_id == setor))
    if dupli.length() > 0:
        raise Exception("ja colocado")

