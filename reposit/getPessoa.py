from select import select
from db_instance import db
from model.Pessoa import Pessoa

def getPessoa(cpf):
    pessoa = Pessoa()
    stmt = (select(pessoa.nome,
                   pessoa.c.idade,
                   pessoa.c.sexo
            ).where(pessoa.cpf == cpf)
            )
    result = db.session.execute(stmt)
    return result

def getPessoas():
    return db.session.scalars(Pessoa).all()