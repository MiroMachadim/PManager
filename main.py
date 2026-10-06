import flask
import os
import dotenv

dotenv.load_dotenv()
app = flask.Flask(__name__)
flask.Flask.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return "funcionando"

if __name__ == "__main__":
    app.run(debug=True)