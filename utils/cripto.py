from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def criptografarSenha(senha):
    return pwd_context.encrypt(senha)


def verficiarSenha(senha, senhaCript):
    try:
        return pwd_context.verify(senha, senhaCript)
    except Exception:
        return False


