import reposit.conexao_banco as cb
import model
import reposit.busca_banco as busca
from db_instance import db
from datetime import datetime

def pedir_ocorrencias(id=None, cpf=None, crime=None, data=None):
    from db_instance import db
    from model.Ocorrencia import Bo
    from model.Tipo import Tipo

    if id:
        return db.session.scalar(db.select(Bo).where(Bo.id == id))   # UM objeto Bo

    stmt = db.select(Bo)
    condicoes = []
    if cpf:
        condicoes.append(Bo.cpf_vitima.ilike(f"%{cpf}%"))
    if crime:
        stmt = stmt.join(Tipo, Bo.tipo_id == Tipo.id)
        condicoes.append(Tipo.nome.ilike(f"%{crime}%"))
    if data:
        try:
            data = datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            return False
        condicoes.append(Bo.created_at == data)
    if condicoes:
        filtro = condicoes[0]
        for c in condicoes[1:]:
            filtro &= c
        stmt = stmt.where(filtro)

    return db.session.scalars(stmt.order_by(Bo.created_at.desc())).all()

def listar_ocorrencias():
    from model.Ocorrencia import Bo
    return db.session.scalar(db.select(Bo).order_by(Bo.created_at.desc())).all()


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
        condicoes.append(Pessoa.cpf.ilike(f"%{cpf}%"))

    if nome:
        condicoes.append(Pessoa.nome.ilike(f"%{nome}%"))

    if condicoes:
        filtro = condicoes[0]
        for c in condicoes[1:]:
            filtro &= c
        stmt = stmt.where(filtro)

    return busca.executar_join(stmt)