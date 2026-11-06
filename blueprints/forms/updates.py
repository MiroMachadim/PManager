from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user, login_required
from service.list_service import pedir_ocorrencias
from service.sender_service import atualizar_ocorrencia
import reposit.busca_banco as be

update_bp = Blueprint('update', __name__)

@update_bp.route('/upd_ocorrencia/<int:id>', methods=['GET','POST'])
@login_required
def upd_ocorrencia(id):

    ocorrencia = pedir_ocorrencias(id)

    if not ocorrencia:
        flash('Ocorrência não encontrada.', 'danger')
        return redirect(url_for('lista.list_ocorrencia'))

    if request.method == 'POST':

        dados = dict()
        dados["id"] = id
        dados["estado_id"] = request.form.get("status")
        dados["cidade"] = request.form.get("cidade")
        dados["tipo_id"] = request.form.get("tipo_crime")
        dados["cpf_vitima"] = request.form.get("cpf_vitima")
        dados["conteudo"] = request.form.get("descricao")
        dados["updated_by"] = current_user.id
        atualizar_ocorrencia(dados)
        flash('Ocorrência atualizada com sucesso!', 'success')
        return redirect(url_for('lista.list_ocorrencia'))

    return render_template('editar_ocorrencia.html', ocorrencia=ocorrencia, tipos=be.listar_tipo(), status_list=be.listar_Estado())