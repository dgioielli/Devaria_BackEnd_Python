from dtos.BaseDTO import BaseDTO

class LoginDTO(BaseDTO):
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

