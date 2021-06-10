from flask import Blueprint, Response
from flask_restx import Namespace, Resource
import config
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioBaseDTO
from utils import decorators

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário')

@api.route('/usuario', methods=['GET'])
class UsuarioController(Resource):

    @decorators.token_required
    def get(self, *args, **kwargs):
        try:
            if 'user_id' in kwargs:
                user_id = kwargs["user_id"]
                return Response(UsuarioBaseDTO("Admin", config.LOGIN_TESTE).dumps(), status=200, mimetype='application/json')
            return Response(UsuarioBaseDTO("admin", config.LOGIN_TESTE).dumps(), status=200, mimetype='application/json')
        except Exception as ex:
            return Response(
                ErroDTO(500, "Não foi possível recuperar o usuário. Tente novamente!" + ex).dumps(),
                status=500,
                mimetype='application/json'
            )