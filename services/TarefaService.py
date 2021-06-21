from database.databese import SessionLocal
from models.Tarefa import Tarefa
from utils.cripto import verficiarSenha

db = SessionLocal()

class TarefaService:
    def __init__(self):
        pass

    def filterByNome(self, nome):
        return db.query(Tarefa).filter(Tarefa.nome == nome).first()

    def filterById(self, id):
        return db.query(Tarefa).filter(Tarefa.id == id).first()

    def criarTarefa(self, nome, dataPrevisao, dataConclusao, idUsuario):

        if self.filterByNome(nome):
            return None

        nova_tarefa = Tarefa(nome=nome, dataPrevisaoConclusao=dataPrevisao, dataConclusao=dataConclusao, idUsuario=idUsuario)

        db.add(nova_tarefa)
        db.commit()

        return nova_tarefa
