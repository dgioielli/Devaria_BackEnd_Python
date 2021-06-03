from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource, fields
from dtos.ErroDTO import ErroDTO

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
            if not body or 'login' not in body or 'senha' not in body:
                return Response(ErroDTO(400, 'Parâmetros de entrada inválido').dumps(), status=400, mimetype='application/json')

            return Response('Login autenticado com sucesso', status=200, mimetype='application/json')
        except Exception as ex:
            return Response(ErroDTO(500, "Não foi possível efetuar o login. Tente novamente!").dumps(), status=500, mimetype='application/json')

