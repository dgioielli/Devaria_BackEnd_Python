from database.databese import SessionLocal
from models.Usuario import Usuario
from utils.cripto import verficiarSenha

db = SessionLocal()

class UsuarioService:
    def __init__(self):
        pass

    def login(self, email, senha):
        usuario = db.query(Usuario).filter(Usuario.email == email).first()

        if not usuario:
            return None

        if not verficiarSenha(senha, usuario.senha):
            return None

        return usuario

    def filterByemail(self, email):
        return db.query(Usuario).filter(Usuario.email == email).first()

    def filterById(self, id):
        return db.query(Usuario).filter(Usuario.id == id).first()

    def criarUsuario(self, nome, email, senha):

        if self.filterByemail(email):
            return None

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)

        db.add(novo_usuario)
        db.commit()

        return novo_usuario