from flask import Blueprint, render_template, request, url_for, redirect
import db_fake

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
       cpf = request.form.get("cpf")
       senha = request.form.get("password")

       usuario_encontrado = None
       for user in db_fake.USUARIOS_FALSOS.values():
           if user["cpf"] == cpf:
               usuario_encontrado = user
               break

       if usuario_encontrado and usuario_encontrado["senha"] == senha:
           if usuario_encontrado["admin"]:
               return redirect(url_for('admin.homepage'))
           else:
               return redirect(url_for("hub.homepage"))
       else:
           return render_template('login.html', erro="CPF ou senha inválidos")

    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    return redirect(url_for('login.login'))