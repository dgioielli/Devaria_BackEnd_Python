from dtos.BaseDTO import BaseDTO

class SucessoDTO(BaseDTO):
    def __init__(self, status, msg):
        self.status = status
        self.msg = msg