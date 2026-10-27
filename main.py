import flask
import os
import dotenv
from ext import login_manager
from db_instance import db
from flask_bcrypt import Bcrypt

dotenv.load_dotenv()
app = flask.Flask(__name__)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
flask.Flask.secret_key = os.getenv("SECRET_KEY")

login_manager.init_app(app)
db.init_app(app)

with app.app_context():
    db.reflect()


if __name__ == "__main__":
    app.run(debug=True)