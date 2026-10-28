from flask import Blueprint, render_template

hub_bp = Blueprint('hub', __name__)

@hub_bp.route('/')
def homepage():
    return render_template("index.html")

@hub_bp.route('/ocorrencias')
def ocorrencias():
    return render_template("ver_ocorrencias.html")
