from datetime import datetime
from symbol import decorator

from flask import Blueprint, Response, request
from flask_restx import Namespace, Resource

from dtos.ErroDTO import ErroDTO
from dtos.SucessoDTO import SucessoDTO
from services.TarefaService import TarefaService
from utils import decorators
from utils.validacao import validar_data

tarefa_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Tarefa')

@api.route('/tarefa', methods=['POST'])
class TarefaController(Resource):

    @decorators.token_required
    def post(self, *args, **kwargs):
        try:
            body = request.get_json()
            erros = []
            if not body:
                return Response(ErroDTO(400, "O body da requisição não pode estra vazio!").dumps(), status=400, mimetype='application/json')
            if 'nome' not in body:
                erros.append("É necessário que seja passado um nome!")
            if 'dataPrevisaoConclusao' not in body:
                erros.append("É necessário que seja passado um dataPrevisaoConclusao!")
            elif not validar_data(body["dataPrevisaoConclusao"]):
                erros.append("Campo 'dataPrevisaoConclusao' inválido, formato deve ser YYYY-mm-dd")
            #elif validar_data(body["dataPrevisaoConclusao"]) < datetime.now:
            #    erros.append("Campo 'dataPrevisaoConclusao' inválido, não pode ser menor do que hoje.")
            if 'dataConclusao' not in body:
                erros.append("É necessário que seja passado um dataConclusao!")

            if len(erros) > 0:
                return Response(ErroDTO(400, erros).dumps(), status=200, mimetype='application/json')

            tarefa_criada = TarefaService().criarTarefa(body["nome"], body["dataPrevisaoConclusao"], None, kwargs["user"].id)

            if not tarefa_criada:
                return Response(ErroDTO(400, "Já existe uma tarefa com esse nome no sistema!").dumps(),
                    status=400,
                    mimetype='application/json')

            return Response(tarefa_criada.to_dict(), status=200, mimetype='application/json')
        except Exception as ex:
            return Response(
                ErroDTO(500, "Não foi possível recuperar o usuário. Tente novamente!" + ex).dumps(),
                status=500,
                mimetype='application/json'
            )
        pass