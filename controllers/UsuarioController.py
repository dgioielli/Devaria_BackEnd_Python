from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource
import config
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioBaseDTO, UsuarioCreateDTO
from services.UsuarioService import UsuarioService
from utils import decorators
from utils.cripto import criptografarSenha

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário')

@api.route('/usuario', methods=['GET', 'POST'])
class UsuarioController(Resource):

    @decorators.token_required
    def get(self, *args, **kwargs):
        try:
            if 'user' in kwargs:
                user = kwargs["user"]
                return Response(UsuarioBaseDTO(user.nome, user.email).dumps(), status=200, mimetype='application/json')
            return Response(ErroDTO(401, "Acesso Negado!").dumps(), status=200, mimetype='application/json')
        except Exception as ex:
            return Response(
                ErroDTO(500, "Não foi possível recuperar o usuário. Tente novamente!" + ex).dumps(),
                status=500,
                mimetype='application/json'
            )

    def post(self):
        try:
            # receber os parâmetros do body da requisição
            body = request.get_json()

            erros = []

            if not body:
                return Response(ErroDTO(400, "O body da requisição não pode estra vazio!").dumps(), status=400, mimetype='application/json')
            if 'nome' not in body:
                erros.append("É necessário que seja passado um name!")
            if 'email' not in body:
                erros.append("É necessário que seja passado um email!")
            if 'senha' not in body:
                erros.append("É necessário que seja passada uma senha!")

            if len(erros) > 0:
                return Response(ErroDTO(400, erros).dumps(), status=400, mimetype='application/json')

            senhaCript = criptografarSenha(body['senha'])

            usuario_criado = UsuarioService().criarUsuario(body["nome"], body["email"], senhaCript)

            if not usuario_criado:
                return Response(
                    ErroDTO(400, "e-mail já cadastrado no sistema!").dumps(),
                    status=400,
                    mimetype='application/json')

            return Response(
                UsuarioCreateDTO(usuario_criado.nome, usuario_criado.email, usuario_criado.senha).dumps(),
                status=201,
                mimetype='application/json'
            )
            pass
        except Exception as ex:
            return Response(
                ErroDTO(500, "Não foi possível recuperar o usuário. Tente novamente!" + ex).dumps(),
                status=500,
                mimetype='application/json'
            )