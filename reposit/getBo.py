from select import select
from db_instance import db
from model.Ocorrencia import Bo

def getBo(id):
    bo = db.get_or_404(Bo,id)
    return bo

def getBoDate(date):
    bo = Bo()
    stmt = select(bo).where(bo.created_at == date).order_by(bo.created_at).all()
    result = db.session.scalars(stmt).fetchall()
    return result