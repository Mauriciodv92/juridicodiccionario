from werkzeug.security import generate_password_hash, check_password_hash

# Usuario administrador quemado para simplificar
USERS = {
    "admin": generate_password_hash("admin123")
}

def validar_usuario(usuario, clave):
    if usuario in USERS and check_password_hash(USERS[usuario], clave):
        return True
    return False
