import flask
import os
import dotenv
from flask import render_template
from jinja2.loaders import split_template_path

from ext import login_manager
from db_instance import db

dotenv.load_dotenv()
app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
flask.Flask.secret_key = os.getenv("SECRET_KEY")

login_manager.init_app(app)
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  # Substitua "User" pelo nome real da classe do modelo de utilizador no vosso banco
  return Pessoa.query.get(int(user_id))

with app.app_context():
    db.reflect()

@app.route("/")
def index():
    return render_template("editar_ocorrencia.html")
# Solução provisoria só para ver como estavão as paginas
# Se quiser ver como ficou as Páginas só copiar daqui:
# cadastrar_ocorrencia.html
# editar_ocorrecia.html
# falta.html
# ficha_criminal.html
# index.html
# listar_ocorrencias.html
# login.html
# ver_ocorrencias.html

if __name__ == "__main__":
    app.run(debug=True)