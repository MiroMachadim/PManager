from model.Policial import Policial
from model.Pessoa import Pessoa
from service.crypt_service import encriptar_senha
import reposit.conexao_banco as cb
def inserir_oficial(dados: dict):
    senha = dados.get('senha')
    encriptada = encriptar_senha(senha)
    dados.update({'senha': encriptada})
    return cb.inserir_dados(Policial, dados, 4)

def atualizar_oficial(dados: dict):
    oficial = cb.instanciar(Policial,dados.get('id'))
    senha = dados.get('senha')
    if senha:
        dados.update({'senha':encriptar_senha(senha)})
    return cb.inserir_dados(oficial, dados, 4)

def atualizar_pessoa(dados: dict):
    pessoa = cb.instanciar(Pessoa, dados.get('cpf'))
    return cb.inserir_dados(pessoa, dados, 4)

def inserir_pessoa(dados: dict):
    return cb.inserir_dados(Pessoa, dados, 4)
