from flask import Blueprint, render_template, request, url_for, redirect, flash
import service.list_service as listar
from service.sender_service import adquirir_cpf
from blueprints.hubs.hubs import ocorrencias

view_bp = Blueprint('view', __name__)

@view_bp.route('/view/<cpf>', methods=['GET','POST'])
def ficha(cpf):
    cpf_limpo = adquirir_cpf(cpf)
    pessoa = listar.pedir_pessoa(cpf_limpo)
    if not pessoa:
        flash("Pessoa não existente no sistema")
        return redirect(url_for("listas.list_fichas"))
    boletins = listar.pedir_ocorrencia_ficha(cpf_limpo)
    return render_template("ficha_criminal.html", pessoa=pessoa, ocorrencias=boletins)
