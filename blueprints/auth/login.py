from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/fazer_login')
def login():
    return "paglogin"
@user_bp.route('/')
def index():
    return "pagina inicial"