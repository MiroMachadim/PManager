import os
from flask import redirect, url_for, flash
import reposit.conexao_banco as cb
import reposit.insercao_banco as ib
import reposit.busca_banco as bb
import service.crypt_service as pc
from model.Cargo import Cargo


def cadastro_oficial(dados: dict):
    from model.Policial import Policial

    cpf = dados.get("cpf")
    cpf_bruto = adquirir_cpf(cpf)
    dados.update({"cpf": cpf_bruto})

    cargo = dados.get("cargo")
    cargo_id = bb.id_por_nome(Cargo, cargo)
    dados.update({"cargo_id": cargo_id})
    dados.pop("cargo")
    if cargo_id == 1:
        dados.update({"admin":True})
    else:
        dados.update({"admin":False})

    oficial_existente = cb.selecionar_por_cpf(Policial, cpf_bruto)

    if oficial_existente:
        flash("CPF já cadastrado", "warning")
        return redirect(url_for("admin.cadastrar_policial"))

    sucesso = ib.inserir_oficial(dados)
    if sucesso:
        flash("Oficial cadastrado com sucesso", "success")
        return redirect(url_for("admin.hub_admin"))
    else:
        flash("Erro ao cadastrar oficial", "error")
        return redirect(url_for("admin.cad_policial"))


def listar_policial(cpf=None, nome=None, cidade=None) -> list:
    from db_instance import db
    from model.Policial import Policial
    from model.Pessoa import Pessoa

    stmt = db.select(Policial)
    condicoes = []

    if cpf:
        cpf_limpo = adquirir_cpf(cpf)
        condicoes.append(Policial.cpf.ilike(f"%{cpf_limpo}%"))

    if nome:
        stmt = stmt.join(Pessoa, Policial.cpf == Pessoa.cpf)
        condicoes.append(Pessoa.nome.ilike(f"%{nome}%"))

    if cidade:
        condicoes.append(Policial.cidade.ilike(f"%{cidade}%"))

    if condicoes:
        filtro = condicoes[0]
        for c in condicoes[1:]:
            filtro = filtro & c
        stmt = stmt.where(filtro)

    return db.session.scalars(stmt).all()

def atualizar_oficial(dados: dict):
    from flask import request
    cargo = dados.get("cargo")
    cargo_id = bb.id_por_nome(Cargo, cargo)
    dados.update({"cargo_id": cargo_id})
    dados.pop("cargo")

    senha = dados.get("senha")
    if senha:
        dados.update({"senha":pc.encriptar_senha(senha)})
    status = ib.atualizar_oficial(dados)
    if status:
        flash("Perfil atualizado com sucesso", "success")
    else:
        flash("Algo deu errado, tente novamente", "error")

    return redirect(request.referrer or url_for("admin.list_perfis"))


def iniciar_edicao(id):
    from model.Policial import Policial

    policial = cb.instanciar(Policial, id)
    if policial is None:
        flash("Policial não encontrado", "warning")
        return False
    return policial



def login_service(dados: dict):
    from model.Policial import Policial

    cpf_bruto = dados.get("cpf")
    if cpf_bruto == os.getenv("ADMIN_CPF"):
        admin_pass = True
    else:
        admin_pass = False
    cpf = adquirir_cpf(cpf_bruto)
    senha = dados.get("senha")

    oficial = cb.selecionar_por_cpf(Policial, cpf)

    if oficial:
        senha_hash = oficial.senha
        if pc.verificar_senha(senha, senha_hash, admin_pass):
            return oficial
        else:
            return False
    else:
        return False


def adquirir_cpf(cpf):
    if cpf:
        return cpf.replace(".", "").replace("-", "")
    return cpf