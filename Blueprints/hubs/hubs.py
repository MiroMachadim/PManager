from flask import Blueprint, render_template
from flask_login import login_required

hub_bp = Blueprint('hub', __name__)

@hub_bp.route('/')
@login_required
def homepage():
    return render_template("index.html")

@hub_bp.route('/ocorrencias')
@login_required
def ocorrencias():
    return render_template("ver_ocorrencias.html")
