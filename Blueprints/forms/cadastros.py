from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import current_user, login_required
import service.sender_service as sender

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/cad_ocorrencia', methods=['GET','POST'])
@login_required
def cad_ocorrencia():
    if request.method == 'POST':
        dados = dict()
        dados["estado_id"] = request.form.get("estado")
        dados["area_id"] = request.form.get("cidade")
        dados["tipo_id"] = request.form.get("tipo_crime")
        dados["cpf"] = request.form.get("cpf_vitima")
        dados["conteudo"] = request.form.get("descricao")
        dados["created_by"] = current_user.id

        enviado = sender.cadastrar_ocorrencia(dados)

        if enviado:
            return redirect(url_for("hub.homepage"))
        else:
            return render_template("cadastrar_ocorrencia.html", msg="envio de bo falhou, tente novamente")

    return render_template("cadastrar_ocorrencia.html")

@cadastro_bp.route('/cad_falta', methods=['GET','POST'])
@login_required
def cad_falta():
    if request.method == 'POST':
        dados = dict()
        dados["data_inicio"] = request.form.get("data_inicio")
        dados["data_fim"] = request.form.get("data_fim")
        dados["arquivo_falta"] = request.files.get("arquivo_comprovante")
        dados["policial_id"] = current_user.id
        if sender.enviar_falta(dados):
           return redirect(url_for("hub.homepage"))
    return render_template("cadastrar_falta.html")
