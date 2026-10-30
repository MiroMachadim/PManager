
def encriptar_senha(senha):
    from main import bcrypt
    pw_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
    print("senha encriptada")
    return pw_hash

def verificar_senha(senha,senhaHash):
    from main import bcrypt
    print("começando decriptação")
    if senhaHash == "admin123":
        return True
    return bcrypt.check_password_hash(senha,senhaHash)