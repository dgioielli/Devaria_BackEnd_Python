from dtos.BaseDTO import BaseDTO


class UsuarioBaseDTO(BaseDTO):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UsuarioLoginDTO(UsuarioBaseDTO):
    def __init__(self, name, email, token):
        super().__init__(name, email)
        self.token = token

