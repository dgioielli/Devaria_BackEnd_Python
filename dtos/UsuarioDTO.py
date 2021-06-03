from dtos.BaseDTO import BaseDTO

class LoginDTO(BaseDTO):
    def __init__(self, name, email, token):
        self.name = name
        self.email = email
        self.token = token

