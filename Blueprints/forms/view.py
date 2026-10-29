from flask import Blueprint, render_template, request, url_for, redirect
import service.list_service as listar
from Blueprints.hubs.hubs import ocorrencias

view_bp = Blueprint('view', __name__)

@view_bp.route('/view/<cpf>', methods=['GET','POST'])
def ficha(cpf):
    pessoa = listar.pedir_pessoa(cpf)
    boletins = listar.listar_bo_ficha(cpf)
    return render_template("ficha_criminal.html", pessoa=pessoa, ocorrencias=boletins)
