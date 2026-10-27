from select import select
from flask import redirect, url_for, render_template
import reposit.conexao_banco as cb
import reposit.insercao_banco as ib
import reposit.busca_banco as bb
from model.Policial import Policial


def cadastro_oficial(dados:dict):
    cpf = dados.get('cpf')
    oficiais = cb.selecionar_por_cpf(Policial(), cpf)
    if oficiais:
        ib.inserir_oficial(dados)
        return redirect(url_for("admin.hub._admin",msg="inserido com sucesso"))
    else:
        return redirect(url_for("cadastrar_policial",msg="oficial ja inserido"))

def listar_policial(cpf, zona,cargo) -> list:
    policial = Policial()
    stmt = select(Policial()).where(policial.c.cpf==cpf,policial.c.zona == zona,policial.c.cargo==cargo)
    return bb.buscar(stmt)

def atualizar_oficial(dados: dict):
    status = ib.atualizar_oficial(dados)
    if not status:
        return redirect(url_for("admin.list_perfis",msg="algo deu errado, tente novamente"))

def iniciar_edicao(id):
    policial = cb.instanciar(Policial(),id)
    return render_template("editar_policial.html", policial=policial)
