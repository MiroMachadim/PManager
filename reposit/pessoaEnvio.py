from db_instance import db
import model.Pessoa


def enviarPessoa(cpf, nome, idade, sexo):
    pessoa = model.Pessoa.Pessoa()
    pessoa.cpf = cpf
    pessoa.nome = verificarNome(nome)
    pessoa.idade = idade
    pessoa.sexo = sexo
    db.session.add(pessoa)

    return db.session.commit()

def verificarNome(nome):
    for letra in nome:
        if letra == ' ' and letra.isalpha():
            continue
        else:
            raise Exception()
    return nome
