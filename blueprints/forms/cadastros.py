from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user, login_required
import service.sender_service as sender
import reposit.busca_banco as be

cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/cad_ocorrencia', methods=['GET','POST'])
@login_required
def cad_ocorrencia():
    if request.method == 'POST':
        dados = dict()
        dados["estado_id"] = request.form.get("status")
        dados["cidade"] = request.form.get("cidade")
        dados["tipo"] = request.form.get("tipo_crime")
        dados["cpf"] = request.form.get("cpf_vitima")
        dados["conteudo"] = request.form.get("conteudo")
        dados["created_by"] = current_user.id
        print(dados)

        enviado = sender.cadastrar_ocorrencia(dados)

        if enviado:
            bo_id = enviado
            suspeito = request.form.get("suspeitos","")
            if suspeito:
                if sender.inserir_suspeito(suspeito,bo_id):
                    flash("enviado com sucesso")
                else:
                    flash("AVISO:culpado não enviado")
            return redirect(url_for("hub.homepage"))
        else:
            flash("deu algum erro no envio")
            return redirect(url_for("cadastro.cad_ocorrencia"))

    print(be.listar_tipo())
    print(be.listar_Estado())
    return render_template("cadastrar_ocorrencia.html", tipos=be.listar_tipo(), status_list=be.listar_Estado())

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
        else:
            return redirect(url_for("cadastro.cad_falta"))
    print(current_user.id)
    return render_template("cadastrar_falta.html")
