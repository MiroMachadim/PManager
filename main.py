import flask
import os
import dotenv
from Blueprints.admin.admin import admin_bp
from Blueprints.auth.login import login_bp
from Blueprints.forms.cadastros import cadastro_bp
from Blueprints.forms.updates import update_bp
from Blueprints.forms.view import view_bp
from Blueprints.hubs.hubs import hub_bp
from Blueprints.list.listas import lista_bp
from ext import login_manager
from db_instance import db
from flask_bcrypt import Bcrypt

dotenv.load_dotenv()

ALLOWED_EXTENSIONS = {"pdf","docx"}
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
app = flask.Flask(__name__)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ALLOWED_EXTENSIONS
flask.Flask.secret_key = os.getenv("SECRET_KEY")

login_manager.init_app(app)
db.init_app(app)

with app.app_context():
    db.reflect()

app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(cadastro_bp, url_prefix="/cadastro")
app.register_blueprint(update_bp, url_prefix="/update")
app.register_blueprint(view_bp, url_prefix="/view")
app.register_blueprint(hub_bp, url_prefix="/hub")
app.register_blueprint(lista_bp, url_prefix="/lista")

if __name__ == "__main__":
    app.run(debug=True)