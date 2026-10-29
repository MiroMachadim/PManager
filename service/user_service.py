from select import select
from flask import redirect, url_for, render_template
import reposit.conexao_banco as cb
import reposit.insercao_banco as ib
import reposit.busca_banco as bb
import service.crypt_service as pc


def cadastro_oficial(dados:dict):
    from model.Policial import Policial
    cpf = dados.get('cpf')
    oficiais = cb.selecionar_por_cpf(Policial(), cpf)
    if oficiais:
        ib.inserir_oficial(dados)
        return redirect(url_for("admin.hub._admin",msg="inserido com sucesso"))
    else:
        return redirect(url_for("cadastrar_policial",msg="oficial ja inserido"))

def listar_policial(cpf, zona,cargo) -> list:
    from model.Policial import Policial
    policial = Policial()
    ilikecpf = '%' + cpf + '%'
    ilikezona = '%' + zona + '%'
    ilikecargo = '%' + cargo + '%'
    stmt = select(Policial()).where(policial.c.cpf.ilike(ilikecpf),policial.c.zona.ilike(ilikezona),policial.c.cargo.ilike(ilikecargo))
    return bb.buscar(stmt)

def atualizar_oficial(dados: dict):
    status = ib.atualizar_oficial(dados)
    if not status:
        return redirect(url_for("admin.list_perfis",msg="algo deu errado, tente novamente"))

def iniciar_edicao(id):
    from model.Policial import Policial
    policial = cb.instanciar(Policial(),id)
    return render_template("editar_policial.html", policial=policial)

def login_service(dados:dict):
    from model.Policial import Policial
    cpf = dados.get('cpf')
    senha = dados.get('senha')
    existe = cb.listar_por_cpf(Policial(), cpf)
    if existe:
        senhaHash = existe[0].senha
        if pc.verificar_senha(senha,senhaHash):
            return existe[0]
    else:
        return False

