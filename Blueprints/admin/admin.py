from flask import Blueprint, render_template, request, redirect, url_for

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def homepage():
    return render_template("home_admin.html")

@admin_bp.route('/hub_admin')
def hub_admin():
    return render_template("ver_opcoes_admin.html")

@admin_bp.route('/cad_policial', methods=['GET','POST'])
def cad_policial():
    # policial = Instancia a tabela aqui
    policial = {
        "cpf" : "123"
    }
    if request.method == 'POST':
        dados = dict()
        dados["nome"] = request.form.get('nome_completo')
        dados["cpf"] = request.form.get('cpf')
        dados["cargo"] = request.form.get('cargo')
        dados["zona"] = request.form.get('zona')
        dados["senha"] = request.form.get('senha_provisoria')
        if policial["cpf"] != cpf:
            if nome and cargo and zona and senha:
                print(nome, cargo, zona, cpf, senha)
                return redirect(url_for("admin.hub_admin"))
            else:
                return render_template("cadastrar_policial.html")
        else:
            return render_template("cadastrar_policial.html", erro = "Esse CPF já está atrelado a um perfil.")
    return render_template("cadastrar_policial.html")

@admin_bp.route('/list_perfis', methods=['GET','POST'])
def list_perfis():
    # policiais = Miro coloca aqui a table dos policiais

    policiais = [
        {
            "id": 1,
            "nome" : "Vandra Volkovenn",
            "cpf": "243.456.789-00",
            "cargo": "Capitão",
            "zona": "norte"
        },
        {
            "id": 2,
            "nome" : "Allan Veiger",
            "cpf": "243.456.789-99",
            "cargo": "Capitão",
            "zona": "norte"
        },
    ]

    filtro_cpf = request.args.get('cpf')
    filtro_nome = request.args.get('nome')
    filtro_zona = request.args.get('zona')

    print(filtro_cpf, filtro_nome, filtro_zona)


    return render_template("listar_perfis.html", policiais=policiais)

@admin_bp.route('/upd_policial/<int:id>', methods=['GET','POST'])
def upd_policial(id):
    # policial = Miro coloca aqui a table dos policiais

    policial = {
            "id": 1,
            "nome": "Policial com nome foda",
            "zona": "Cz",
            "sexo": "F",
            "cargo": "recruta",
            "data_nascimento": "05/10/2030",
            "cpf": "198.034.132-44"
        }

    if request.method == 'POST':
        # policial.cargo = request.form.get("estado") COLOCA TODOS A BAIXO NESSE PADRÂO

        cargo = request.form.get("cargo")
        zona = request.form.get("zona")

        senha_nova = request.form.get("senha")
        if senha_nova:
            senha = senha_nova

        #db.session.commit()
        return redirect(url_for("admin.list_perfis"))

    return render_template("editar_policial.html",policial=policial)