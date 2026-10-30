import flask
import os
import dotenv
from ext import login_manager
from db_instance import db
from flask_bcrypt import Bcrypt

dotenv.load_dotenv()

app = flask.Flask(__name__)

# 3. Configurações da App
ALLOWED_EXTENSIONS = {"pdf", "docx"}
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")  # Corrigido!
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Recomendado mudar para False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ALLOWED_EXTENSIONS

bcrypt = Bcrypt(app)
login_manager.init_app(app)
db.init_app(app)


with app.app_context():
    db.reflect()

import model.Policial
from Blueprints.admin.admin import admin_bp
from Blueprints.auth.login import login_bp
from Blueprints.forms.cadastros import cadastro_bp
from Blueprints.forms.updates import update_bp
from Blueprints.forms.view import view_bp
from Blueprints.hubs.hubs import hub_bp
from Blueprints.list.listas import lista_bp

app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(update_bp)
app.register_blueprint(view_bp)
app.register_blueprint(hub_bp)
app.register_blueprint(lista_bp)

if __name__ == "__main__":
    app.run(debug=True)