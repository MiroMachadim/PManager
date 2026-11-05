import reposit.conexao_banco as cb
import model
import reposit.busca_banco as busca
from sender_service import adquirir_cpf
from db_instance import db


def pedir_ocorrencias():
    return cb.listar(model.Ocorrencia.Bo)

def pedir_ocorrencia_ficha(cpf):
    return busca.OcorrenciaFicha(cpf)


def pedir_pessoa(cpf):
    return cb.selecionar_por_cpf(model.Pessoa.Pessoa, cpf)


def listar_bo_ficha(cpf):
    from model.Ocorrencia import Bo
    return busca.buscar(Bo, Bo.cpf_vitima == cpf)


def listar_fichas(cpf=None , nome=None):
    from model.Pessoa import Pessoa
    from model.Ficha import Ficha

    stmt = (
        db.select(
            Pessoa.nome.label("nome"),
            Pessoa.cpf.label("cpf"),
            Pessoa.data_nascimento.label("data_nascimento"),
        )
        .join(Ficha, Ficha.cpf == Pessoa.cpf)
        .distinct()
    )

    condicoes = []

    if cpf:
        condicoes.append(Pessoa.cpf.ilike(f"%{adquirir_cpf(cpf)}%"))

    if nome:
        condicoes.append(Pessoa.nome.ilike(f"%{nome}%"))

    if condicoes:
        filtro = condicoes[0]
        for c in condicoes[1:]:
            filtro &= c
        stmt = stmt.where(filtro)

    return busca.executar_join(stmt)