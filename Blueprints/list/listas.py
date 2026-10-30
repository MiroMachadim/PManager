# import query
from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required

import service.list_service as ls

lista_bp = Blueprint('lista', __name__)

@lista_bp.route('/list_ocorrencia', methods=['GET','POST'])
@login_required
def list_ocorrencia():

    # ocorrencias = "Miro coloca aqui a table das ocorrencias"
    ocorrencias = ls.pedir_ocorrencias()

    filtro_cpf = request.args.get('cpf')
    filtro_tipo_crime = request.args.get('crime')
    filtro_data = request.args.get('data')

    print(filtro_cpf,filtro_tipo_crime,filtro_data)

    #Configurar a query quando estiver com o bd funcionando para utilizar os filtros da pagina

    # if filtro_cpf:
    #     query = query.filter(all_ocorrencias.?.ilike(f"%{filtro_cpf}%"))
    # if filtro_tipo_crime:
    #     query = query.filter(all_ocorrencias.?.ilike(f"%{filtro_tipo_crime}%"))
    # if filtro_data:
    #     query = query.filter(all_ocorrencias.?.ilike(f"%{filtro_data}%"))
    #all_ocorrencias = query.all()


    return render_template('listar_ocorrencias.html', ocorrencias=ocorrencias)

@lista_bp.route('/list_fichas', methods=['GET','POST'])
@login_required
def list_fichas():

    fichas = ls.listar_fichas()
    filtro_cpf = request.args.get('cpf')
    filtro_nome = request.args.get('nome')

    print(filtro_cpf,filtro_nome)


    return render_template('listar_ficha_criminal.html', individuos=fichas)