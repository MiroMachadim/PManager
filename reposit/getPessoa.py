from select import select
from db_instance import db
from model.Pessoa import Pessoa

def get_pessoa(cpf):
    pessoa = Pessoa()
    stmt = (select(pessoa.nome,
                   pessoa.c.idade,
                   pessoa.c.sexo
            ).where(pessoa.cpf == cpf)
            )
    result = db.session.execute(stmt)
    return result

def get_pessoas():
    return db.session.scalars(Pessoa).all()