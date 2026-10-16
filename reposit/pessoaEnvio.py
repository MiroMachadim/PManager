from db_instance import db
import model.Pessoa


def enviar_pessoa(cpf, nome, idade, sexo):
    pessoa = model.Pessoa.Pessoa()
    pessoa.c.cpf = cpf
    pessoa.c.nome = verificar_nome(nome)
    pessoa.c.idade = idade
    pessoa.c.sexo = sexo
    db.session.add(pessoa)

    return db.session.commit()

def verificar_nome(nome):
    for letra in nome:
        if letra == ' ' and letra.isalpha():
            continue
        else:
            raise Exception()
    return nome
