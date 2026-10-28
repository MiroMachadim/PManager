from flask import Blueprint, render_template, request, url_for, redirect
# from sqlalchemy import func, extract
# # Certifique-se de importar o seu 'db' e o seu Model 'Ocorrencia' corretamente:
# # from seu_projeto.models import db, Ocorrencia
grafico_bp = Blueprint('grafico', __name__)
# =============================================================
# ROTA GERADA VIA IA, PARA ORIENTAÇÃO CASO QUEIRA IMPLEMENTALA
# =============================================================
@grafico_bp.route('/grafico')
def grafico():
    # dados_zonas = db.session.query(
    #     Ocorrencia.cidade, func.count(Ocorrencia.id)
    # ).group_by(Ocorrencia.cidade).all()
    #
    # labels_zonas = [item[0] for item in dados_zonas if item[0] is not None]
    # valores_zonas = [item[1] for item in dados_zonas if item[0] is not None]
    #
    # # 2. Gráfico Por Tipos de Crime
    # dados_crimes = db.session.query(
    #     Ocorrencia.tipo_crime, func.count(Ocorrencia.id)
    # ).group_by(Ocorrencia.tipo_crime).all()
    #
    # labels_crimes = [item[0] for item in dados_crimes if item[0] is not None]
    # valores_crimes = [item[1] for item in dados_crimes if item[0] is not None]
    #
    # # 3. Tempo - Agrupado por Ano (Visão Anual Real)
    # dados_anos = db.session.query(
    #     extract('year', Ocorrencia.data_registro).label('ano'),
    #     func.count(Ocorrencia.id)
    # ).group_by('ano').order_by('ano').all()
    #
    # labels_anos = [str(int(item[0])) for item in dados_anos if item[0] is not None]
    # valores_anos = [item[1] for item in dados_anos if item[0] is not None]
    #
    # # 4. Tempo - Agrupado por Mês do Ano Atual (2026)
    # meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    #
    # dados_meses = db.session.query(
    #     extract('month', Ocorrencia.data_registro).label('mes'),
    #     func.count(Ocorrencia.id)
    # ).filter(extract('year', Ocorrencia.data_registro) == 2026) \
    #     .group_by('mes').order_by('mes').all()
    #
    # labels_meses = [meses_nomes[int(item[0]) - 1] for item in dados_meses if item[0] is not None]
    # valores_meses = [item[1] for item in dados_meses if item[0] is not None]
    #
    # # 5. Intervalo Dinâmico de Anos para os inputs da view
    # menor_ano = db.session.query(func.min(extract('year', Ocorrencia.data_registro))).scalar()
    # maior_ano = db.session.query(func.max(extract('year', Ocorrencia.data_registro))).scalar()
    #
    # ano_inicio_padrao = int(menor_ano) if menor_ano else 2023
    # ano_fim_padrao = int(maior_ano) if maior_ano else 2026

    # 6. Renderiza o template passando as variáveis dinâmicas do banco
    return render_template(
        'grafico_ocorrencias.html',)
    #     labels_zonas=labels_zonas,
    #     valores_zonas=valores_zonas,
    #     labels_crimes=labels_crimes,
    #     valores_crimes=valores_crimes,
    #     labels_anos=labels_anos,
    #     valores_anos=valores_anos,
    #     labels_meses=labels_meses,
    #     valores_meses=valores_meses,
    #     ano_inicio_padrao=ano_inicio_padrao,
    #     ano_fim_padrao=ano_fim_padrao
    # )