from chain import chain
from model.Pessoa import Pessoa
from model.Policial import Policial
from reposit import conexao_banco
from service.crypt_service import encriptar_senha



def inserir_pessoa(dados: dict):
   pessoa = Pessoa()
   return conexao_banco.inserir_dados(pessoa, dados, 4)

def atualizar_pessoa(dados: dict):
    pessoa = conexao_banco.instanciar(Pessoa, dados.get('cpf'))
    return conexao_banco.inserir_dados(pessoa, dados, 4)

def inserir_oficial(dados: dict):
    policial = Policial()
    senha = dados.get('senha')
    encriptada = encriptar_senha(senha)
    dados.update({'senha': encriptada})
    return conexao_banco.inserir_dados(policial, dados, 4)

def atualizar_oficial(dados: dict):
    oficial = conexao_banco.instanciar(Policial, dados.get('id'))
    senha = dados.get('senha')
    if senha:
        dados.update({'senha':encriptar_senha(senha)})
    return conexao_banco.inserir_dados(oficial, dados, 4)

def listar_oficiais() -> list:
    oficiais = conexao_banco.listar(Policial)
    return oficiais

def buscar_oficial(id):
    return conexao_banco.selecionar_por_id(Policial, id)

