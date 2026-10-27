# import query
from flask import Blueprint, render_template, request, url_for, redirect

lista_bp = Blueprint('lista', __name__)

@lista_bp.route('/list_ocorrencia', methods=['GET','POST'])
def list_ocorrencia():

    # ocorrencias = "Miro coloca aqui a table das ocorrencias"

    ocorrencias = [
        {
            "id": 1,
            "data_registro": "2026-06-06 12:00",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_vitima": "123.456.789-00",
            "descricao": "Exemplo de relato de teste.",
            "status": "Em Andamento"
        },
        {
            "id": 2,
            "data_registro": "2026-06-06 12:00",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_vitima": "123.456.789-00",
            "descricao": "Exemplo de relato de teste.",
            "status": "Em Andamento"
        }
    ]

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
def list_fichas():

    # fichas = Miro coloca aqui a table das pessoas

    fichas = [
        {
            "id": 1,
            "nome" : "Vandra Volkovenn",
            "cpf": "243.456.789-00",
            "data_nascimento": "2026-06-06 12:00",
        },
        {
            "id": 2,
            "nome" : "Vandra Volksvagens",
            "cpf": "123.456.789-00",
            "data_nascimento": "2026-06-06 12:00",
        }
    ]

    filtro_cpf = request.args.get('cpf')
    filtro_nome = request.args.get('nome')

    print(filtro_cpf,filtro_nome)


    return render_template('listar_ficha_criminal.html', individuos=fichas)