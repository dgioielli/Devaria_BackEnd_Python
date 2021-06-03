from dtos.BaseDTO import BaseDTO

class ErroDTO(BaseDTO):
    def __init__(self, status, erro):
        self.status = status
        self.erro = erro
