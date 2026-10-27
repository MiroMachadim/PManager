import model
from service.crypt_service import encriptar_senha
import conexao_banco as cb

def inserir_oficial(dados: dict):
    policial = model.Policial.Policial()
    senha = dados.get('senha')
    encriptada = encriptar_senha(senha)
    dados.update({'senha': encriptada})
    return cb.inserir_dados(policial, dados, 4)

def atualizar_oficial(dados: dict):
    oficial = cb.instanciar(model.Policial.Policial, dados.get('id'))
    senha = dados.get('senha')
    if senha:
        dados.update({'senha':encriptar_senha(senha)})
    return cb.inserir_dados(oficial, dados, 4)

def atualizar_pessoa(dados: dict):
    pessoa = cb.instanciar(model.Pessoa.Pessoa, dados.get('cpf'))
    return cb.inserir_dados(pessoa, dados, 4)

def inserir_pessoa(dados: dict):
    pessoa = model.Pessoa.Pessoa()
    return cb.inserir_dados(pessoa, dados, 4)
