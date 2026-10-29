from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import current_user, login_required
from service.list_service import pedir_ocorrencias
from service.sender_service import atualizar_ocorrencia

update_bp = Blueprint('update', __name__)

@update_bp.route('/upd_ocorrencia/<int:id>', methods=['GET','POST'])
@login_required
def upd_ocorrencia(id):

    ocorrencia = pedir_ocorrencias()

    if request.method == 'POST':

        # ocorrencia.estado = request.form.get("estado") COLOCA TODOS A BAIXO NESSE PADRÂO

        dados = dict()
        dados["id"] = id
        dados["estado_id"] = request.form.get("estado")
        dados["area_id"] = request.form.get("cidade")
        dados["tipo_id"] = request.form.get("tipo_crime")
        dados["cpf"] = request.form.get("cpf_vitima")
        dados["conteudo"] = request.form.get("descricao")
        dados["updated_by"] = current_user.id
        atualizar_ocorrencia(dados)

        return redirect(url_for('lista.list_ocorrencia'))

    return render_template('editar_ocorrencia.html', ocorrencia=ocorrencia)