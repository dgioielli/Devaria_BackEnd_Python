from functools import wraps

import jwt
from flask import request, Response

from dtos.ErroDTO import ErroDTO
from services import JWTservice


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        headers = request.headers
        if not 'Authorization' in headers:
            return Response(
                ErroDTO(400, "É necessário um token para essa requisição!").dumps(),
                status=400,
                mimetype='application/json'
            )
        try:
            # Pegar Token
            token = str(headers['Authorization']).replace("Bearer ", "")

            user_id = JWTservice.decodificar_token(token)
            kwargs['user_id'] = user_id

        except jwt.ExpiredSignatureError:
            return Response(ErroDTO(401, "Token expirado!").dumps(), status=401, mimetype='application/json')
        except jwt.InvalidTokenError:
            return Response(ErroDTO(401, "Token inválido!").dumps(), status=401, mimetype='application/json')
        except Exception:
            return Response(
                ErroDTO(500, "Erro inesperado no servidor. Tente novamente!").dumps(),
                status=500,
                mimetype='application/json'
            )

        return func(*args, **kwargs)
    return decorated