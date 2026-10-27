from flask import Blueprint, render_template, request, redirect, url_for
import service.user_service as su

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def homepage():
    return render_template("home_admin.html")

@admin_bp.route('/hub_admin')
def hub_admin():
    return render_template("ver_opcoes_admin.html")

@admin_bp.route('/cad_policial', methods=['GET','POST'])
def cad_policial():
    if request.method == 'POST':
        dados = dict()
        dados["nome"] = request.form.get('nome_completo')
        dados["cpf"] = request.form.get('cpf')
        dados["cargo"] = request.form.get('cargo')
        dados["zona"] = request.form.get('zona')
        dados["senha"] = request.form.get('senha_provisoria')
        su.cadastro_oficial(dados)
    return render_template("cadastrar_policial.html")

@admin_bp.route('/list_perfis', methods=['GET','POST'])
def list_perfis():
    filtro_cpf = request.args.get('cpf')
    filtro_nome = request.args.get('nome')
    filtro_zona = request.args.get('zona')

    print(filtro_cpf, filtro_nome, filtro_zona)

    policiais = su.listar_policial(filtro_cpf,filtro_nome,filtro_zona)

    return render_template("listar_perfis.html", policiais=policiais)

@admin_bp.route('/upd_policial/<int:id>', methods=['GET','POST'])
def upd_policial(id):
    # policial = Miro coloca aqui a table dos policiais


    if request.method == 'POST':
        # policial.cargo = request.form.get("estado") COLOCA TODOS A BAIXO NESSE PADRÂO
        dados = dict()
        dados["cpf"] = request.form.get('cpf')
        dados["cargo_id"] = request.form.get("cargo")
        dados["senha"] = request.form.get("senha")
        su.atualizar_oficial(dados)

        return redirect(url_for("admin.list_perfis"))
    else:
        su.iniciar_edicao(id)