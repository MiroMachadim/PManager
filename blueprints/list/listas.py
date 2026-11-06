from flask import Blueprint, render_template, request
from flask_login import login_required
from service.sender_service import adquirir_cpf

import service.list_service as ls

lista_bp = Blueprint('lista', __name__)

@lista_bp.route('/list_ocorrencia', methods=['GET','POST'])
@login_required
def list_ocorrencia():

    print(request.args)
    filtro_cpf = request.args.get("cpf")
    filtro_nome = request.args.get("crime")
    filtro_data = request.args.get("data")

    filtro_cpf = adquirir_cpf(filtro_cpf) if filtro_cpf else None

    ocorrencias = ls.pedir_ocorrencias(cpf=filtro_cpf,crime=filtro_nome,data=filtro_data)

    return render_template('listar_ocorrencias.html', ocorrencias=ocorrencias)

@lista_bp.route('/list_fichas', methods=['GET','POST'])
@login_required
def list_fichas():

    filtro_cpf = request.args.get('cpf')
    filtro_cpf_limpo = adquirir_cpf(filtro_cpf) if filtro_cpf else None
    filtro_nome = request.args.get('nome')
    fichas = ls.listar_fichas(cpf=filtro_cpf_limpo,nome=filtro_nome)

    print(filtro_cpf,filtro_nome)


    return render_template('listar_ficha_criminal.html', individuos=fichas)