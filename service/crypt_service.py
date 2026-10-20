from main import bcrypt

def encriptar_senha(senha):
    pw_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
    print("senha encriptada")
    return pw_hash

def verificar_senha(senha,senhaHash):
    print("começando decriptação")
    return bcrypt.check_password_hash(senha,senhaHash)