from chain import chain
from model.Pessoa import Pessoa
from model.Policial import Policial
from reposit import conexao_banco
from service.crypt_service import encriptar_senha
from db_instance import db


def inserir_dados(tabela: db.Model, dados, total ):
    chain.handle(tabela, dados, total)
    return conexao_banco.enviar(tabela)

def inserir_pessoa(dados: dict):
   pessoa = Pessoa()
   return inserir_dados(pessoa, dados, 4)

def atualizar_pessoa(dados: dict):
    pessoa = conexao_banco.instanciar(Pessoa, dados.get('cpf'))
    return inserir_dados(pessoa, dados, 4)

def inserir_oficial(dados: dict):
    policial = Policial()
    senha = dados.get('senha')
    encriptada = encriptar_senha(senha)
    dados.update({'senha': encriptada})
    return inserir_dados(policial, dados, 4)

def atualizar_policial(dados: dict):
    oficial = conexao_banco.instanciar(Policial, dados.get('id'))
    senha = dados.get('senha')
    if senha:
        dados.update({'senha':encriptar_senha(senha)})
    return inserir_dados(oficial, dados, 4)
