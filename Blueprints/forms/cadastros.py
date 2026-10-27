from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import os

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/cad_ocorrencia', methods=['GET','POST'])
def cad_ocorrencia():
    if request.method == 'POST':
        estado = request.form.get("estado")
        cidade = request.form.get("cidade")
        tipo_crime = request.form.get("tipo_crime")
        cpf = request.form.get("cpf_vitima")
        relato = request.form.get("descricao")

        if estado and cidade and tipo_crime and cpf and relato:
            print(estado, cidade,tipo_crime,cpf,relato)
            return redirect(url_for("hub.homepage"))
        else:
            return render_template("cadastrar_ocorrencia.html")

    return render_template("cadastrar_ocorrencia.html")

@cadastro_bp.route('/cad_falta', methods=['GET','POST'])
def cad_falta():

    diretorio_uploads = 'uploads/faltas'

    if request.method == 'POST':
        data_inicio = request.form.get("data_inicio")
        data_fim = request.form.get("data_fim")
        arquivo_falta = request.files.get("arquivo_comprovante")

        if arquivo_falta and arquivo_falta.filename != "":
            nome_seg = secure_filename(arquivo_falta.filename)
            caminho_arquivo = os.path.join(diretorio_uploads, nome_seg)
            arquivo_falta.save(caminho_arquivo)
            CAMINHO_DO_BANCO = 'Miro c passa o caminho aqui para salvar no bd'
            print(caminho_arquivo + "" + "salvo")
            print(data_inicio, data_fim)
            return redirect(url_for("hub.homepage"))
    return render_template("cadastrar_falta.html")