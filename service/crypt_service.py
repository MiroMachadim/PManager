import os


def encriptar_senha(senha):
    from main import bcrypt
    pw_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
    print("senha encriptada")
    return pw_hash

def verificar_senha(senha, senha_hash, admin_pass: bool):
    from main import bcrypt
    if admin_pass and senha == os.getenv("ADMIN_SENHA"):
        return True
    print("verificando senha")
    try:
        veri = bcrypt.check_password_hash(senha_hash, senha)
        return veri
    except:
        return False