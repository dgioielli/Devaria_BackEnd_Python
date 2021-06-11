from dtos.BaseDTO import BaseDTO


class UsuarioBaseDTO(BaseDTO):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UsuarioCreateDTO(UsuarioBaseDTO):
    def __init__(self, name, email, senha):
        super().__init__(name, email)
        self.senha = senha


class UsuarioLoginDTO(UsuarioBaseDTO):
    def __init__(self, name, email, token):
        super().__init__(name, email)
        self.token = token

