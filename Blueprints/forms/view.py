from flask import Blueprint, render_template, request, url_for, redirect

from Blueprints.hubs.hubs import ocorrencias

view_bp = Blueprint('view', __name__)

@view_bp.route('/view/<int:id>', methods=['GET','POST'])
def ficha(id):

    # ficha = Instacia a tabela aqui
    # ocorrencias = e aqui tbm


    #MODELOS PRONTOS PARA TESTE:

    ficha = {
            "id": 1,
            "nome": "Tanto faz",
            "nome_mae" : "Mãe da pessoa",
            "nome_pai" : "Pai da pessoa",
            "data_nascimento": "2026/06/06",
            "naturalidade": "Brasileira",
            "cpf": "123.456.789-00",
        }

    ocorrencias = [
        {
            "id": 1,
            "data_registro": "20/06/2026",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_culpado" : "123.456.789-00",
            "status": "Em Validação",
        },
        {
            "id": 2,
            "data_registro": "20/06/2026",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_culpado" : "123.456.789-22",
            "status": "Em Validação",
        },
        {
            "id": 3,
            "data_registro": "20/06/2026",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_culpado" : "123.456.789-13",
            "status": "Em Validação",
        },
        {
            "id": 4,
            "data_registro": "20/06/2026",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_culpado" : "123.456.789-00",
            "status": "Em Validação",
        },
    ]

    ocorrencia_valida = []
    print(ocorrencia_valida)

    for culpado in ocorrencias:
        if ficha["cpf"] == culpado["cpf_culpado"]:
            ocorrencia_valida.append(culpado)

    print(ocorrencia_valida)

    return render_template("ficha_criminal.html", pessoa=ficha, ocorrencias=ocorrencia_valida)
