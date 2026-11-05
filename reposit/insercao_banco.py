from model.Policial import Policial
from model.Pessoa import Pessoa
from service.crypt_service import encriptar_senha
import reposit.conexao_banco as cb


def inserir_oficial(dados: dict) -> bool:
    senha = dados.pop('senha', None)
    if senha:
        dados['senha'] = encriptar_senha(senha)
    print(dados.get("senha"))

    print(dados)

    return cb.inserir_dados(Policial, dados, 5)


def atualizar_oficial(dados: dict) -> bool:
    oficial_id = dados.pop('id', None)
    if oficial_id is None:
        raise ValueError("Campo 'id' é obrigatório para atualização")

    oficial = cb.instanciar(Policial, oficial_id)
    if oficial is None:
        return False

    senha = dados.pop('senha', None)
    if senha:
        dados['senha'] = encriptar_senha(senha)

    return cb.inserir_dados(oficial, dados, 4)


def atualizar_pessoa(dados: dict) -> bool:
    cpf = dados.pop('cpf', None)
    if cpf is None:
        raise ValueError("Campo 'cpf' é obrigatório para atualização")

    pessoa = cb.instanciar(Pessoa, cpf)
    if pessoa is None:
        return False

    return cb.inserir_dados(pessoa, dados, 4)


def inserir_pessoa(dados: dict) -> bool:
    return cb.inserir_dados(Pessoa, dados, 4)