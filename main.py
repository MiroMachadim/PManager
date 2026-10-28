import flask
import os
import dotenv
from ext import login_manager
from db_instance import db
from blueprints.auth import login

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


if __name__ == "__main__":
    app.run(debug=True)