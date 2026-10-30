from flask import redirect, url_for, render_template
import reposit.conexao_banco as cb
import reposit.insercao_banco as ib
import reposit.busca_banco as bb
import service.crypt_service as pc


def cadastro_oficial(dados:dict):
    from model.Policial import Policial
    cpf = dados.get('cpf')
    oficiais = cb.selecionar_por_cpf(Policial, cpf)
    if not oficiais:
        ib.inserir_oficial(dados)
        return redirect(url_for("admin.hub._admin"))
    else:
        return redirect(url_for("cadastrar_policial"))

def listar_policial(cpf, zona,cargo) -> list:
    from model.Policial import Policial
    if cpf:
        ilikecpf = '%' + cpf + '%'
    else:
        ilikecpf = '%%'
    if cargo:
        ilikecargo = '%' + cargo + '%'
    else:
        ilikecargo = '%%'
    stmt = (Policial.cpf.ilike(ilikecpf), Policial.cargo_id.ilike(ilikecargo))
    return bb.buscar(Policial,stmt)

def atualizar_oficial(dados: dict):
    status = ib.atualizar_oficial(dados)
    if not status:
        return redirect(url_for("admin.list_perfis",msg="algo deu errado, tente novamente"))

def iniciar_edicao(id):
    from model.Policial import Policial
    policial = cb.instanciar(Policial,id)
    return render_template("editar_policial.html", policial=policial)

def login_service(dados:dict):
    from model.Policial import Policial
    cpf = dados.get('cpf')
    cpf = adquirir_cpf(cpf)
    senha = dados.get('senha')
    existe = cb.selecionar_por_cpf(Policial, cpf)
    if existe:
        senhaHash = existe.senha
        if pc.verificar_senha(senha,senhaHash):
            return existe
        else:
            return False
    else:
        return False

def adquirir_cpf(cpf):
    cpf = cpf.replace(".","")
    return cpf.replace("-","")
