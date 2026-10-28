from flask import Blueprint, render_template, request, url_for, redirect
import service.user_service as su

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
       dados = dict()
       dados["cpf"] = request.form.get("cpf")
       dados["senha"] = request.form.get("password")
       user = su.login_service(dados)
       if user:
          if user.admin:
               return redirect(url_for('admin.homepage'))
          else:
               return redirect(url_for("hub.homepage"))
       else:
           return render_template('login.html', erro="CPF ou senha inválidos")

    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    return redirect(url_for('login.login'))