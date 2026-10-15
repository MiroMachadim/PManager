from select import select
from db_instance import db
from model.Policial import Policial

def getOficial(id):
    policial = Policial()
    stmt = select(policial.cpf,policial.cargo_id).where(policial.id==id)
    result = db.session.execute(stmt).all()
    return result

def getMembros():
    policiais = Policial()
    stmt = select(policiais.cpf,policiais.cargo_id).order_by(policiais.cargo_id)
    result = db.session.scalars(stmt).all()