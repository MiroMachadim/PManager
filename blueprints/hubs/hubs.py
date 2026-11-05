from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

hub_bp = Blueprint('hub', __name__)

@hub_bp.route('/')
@login_required
def homepage():
    if current_user.admin:
        return redirect(url_for("admin.homepage"))
    return render_template("index.html")

@hub_bp.route('/ocorrencias')
@login_required
def ocorrencias():
    return render_template("ver_ocorrencias.html")
