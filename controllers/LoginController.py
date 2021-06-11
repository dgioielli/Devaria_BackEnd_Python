from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource, fields


import config
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioLoginDTO
from services import JWTservice
from services.UsuarioService import UsuarioService

login_controller = Blueprint("login_controller", __name__)

api = Namespace('Login', description='Realizar login na aplicação')

login_fields = api.model("LoginDTO", {
    "login": fields.String,
    "senha": fields.String
})

user_fields = api.model('UsuarioDTO', {
    'name': fields.String,
    'email': fields.String,
    'token': fields.String,
})

@api.route('/login', methods=['POST'])
class Login(Resource):

    @api.response(200, 'Login autenticado com sucesso', user_fields)
    @api.response(400, 'Parâmetros de entrada inválido')
    @api.response(500, 'Não foi possível efetuar o login. Tente novamente!')
    @api.expect(login_fields)
    def post(self):
        # teste de erros inesperados.
        try:
            # receber os parâmetros do body da requisição
            body = request.get_json()

            erros = []

            if not body:
                return Response(ErroDTO(400, "O body da requisição não pode estra vazio!").dumps(), status=400, mimetype='application/json')
            if 'login' not in body:
                erros.append("É necessário que seja passado um login!")
            if 'senha' not in body:
                erros.append("É necessário que seja passada uma senha!")

            if len(erros) > 0:
                return Response(ErroDTO(400, erros).dumps(), status=400, mimetype='application/json')

            usuario_encontrado = UsuarioService().login(body["login"], body["senha"])
            print(usuario_encontrado)

            if not usuario_encontrado:
                return Response(ErroDTO(401, 'login ou senha incorreto').dumps(), status=401, mimetype='application/json')

            token = JWTservice.gerar_token(usuario_encontrado.id)
            return Response(UsuarioLoginDTO(usuario_encontrado.nome, usuario_encontrado.email, token).dumps(), status=200, mimetype='application/json')
        except Exception as ex:
            return Response(ErroDTO(500, "Não foi possível efetuar o login. Tente novamente!" + ex).dumps(), status=500, mimetype='application/json')

