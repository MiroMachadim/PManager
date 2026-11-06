from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
import service.user_service as su
import service.sender_service as se
import reposit.conexao_banco as cb
from model.Policial import admin_required
from model.Tipo import Tipo
from model.Cargo import Cargo
from model.Estado import Estado
from model.Zona import Zona

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@admin_required
def homepage():
    return render_template("home_admin.html")

@admin_bp.route('/hub_admin')
@admin_required
def hub_admin():
    return render_template("ver_opcoes_admin.html")

@admin_bp.route('/cad_policial', methods=['GET','POST'])
@admin_required
def cad_policial():
    if request.method == 'POST':
        dados_oficial = dict()
        dados_pessoa = dict()
        dados_pessoa["nome"] = request.form.get('nome_completo')
        dados_pessoa["cpf"] = request.form.get('cpf')
        dados_pessoa["data_nascimento"] = request.form.get('data_nascimento')
        dados_pessoa["sexo"] = request.form.get('sexo')
        dados_oficial["cpf"] = request.form.get('cpf')
        dados_oficial["cargo"] = request.form.get('cargo')
        dados_oficial["cidade"] = request.form.get('cidade')
        dados_oficial["senha"] = request.form.get('senha_provisoria')
        se.enviar_pessoa(dados_pessoa)
        sucesso = su.cadastro_oficial(dados_oficial)
        if sucesso:
            flash("Oficial cadastrado com sucesso", "success")
            return redirect(url_for("admin.hub_admin"))
        else:
            flash("Erro ao cadastrar oficial", "error")
            return redirect(url_for("admin.cad_policial"))

    return render_template(
    "cadastrar_policial.html",
        cargos=cb.listar(Cargo),
        cidades=cb.listar(Zona),
        erro=None,
    )
@admin_bp.route('/list_perfis', methods=['GET','POST'])
@admin_required
def list_perfis():
    filtro_cpf = request.args.get('cpf')
    filtro_nome = request.args.get('nome')
    filtro_cidade = request.args.get('cidade')

    print(filtro_cpf, filtro_nome, filtro_cidade)

    policiais = su.listar_policial(filtro_cpf,filtro_nome,filtro_cidade)

    return render_template("listar_perfis.html", policiais=policiais)

@admin_bp.route('/upd_policial/<int:id>', methods=['GET','POST'])
@admin_required
def upd_policial(id):


    if request.method == 'POST':
        dados = dict()
        dados["id"] = id
        dados["cargo"] = request.form.get("cargo")
        dados["senha"] = request.form.get("senha")
        dados["cidade"] = request.form.get("cidade")
        su.atualizar_oficial(dados)

        return redirect(url_for("admin.list_perfis"))
    else:
        policial = su.iniciar_edicao(id)

        if policial:
            return render_template("editar_policial.html", policial=policial)
        else:
            return redirect(url_for("admin.list_perfis"))


@admin_bp.route('/upd_estados' , methods=['GET','POST'])
@admin_required
def upd_parametros():

    if request.method == 'POST':
        dados = dict()
        dados["categoria"] = request.form.get("categoria")
        dados["nome"] = request.form.get("nome_item")
        if dados["categoria"] == "cargo":
            posicao = request.form.get("posicao")
            dados["posicao"] = int(posicao) if posicao else None
            total = 2
        else:
            total = 1
        enviado = se.atualizar_parametros(dados, total)
        if enviado:
            flash("cadastrado com sucesso", 'success')
        else:
            flash("deu algum erro", 'warning')
        return redirect(url_for("admin.upd_parametros"))
    tipos_crime_db = cb.listar(Tipo)
    status_db = cb.listar(Estado)
    cargos_db = cb.listar(Cargo)
    return render_template("editar_parametros.html", tipos_crime=tipos_crime_db, lista_status=status_db,cargos=cargos_db)