from flask import Flask
from flask_restx import Api
from flask_cors import CORS
import config
from controllers.LoginController import login_controller
from controllers.LoginController import api as ns_login
from controllers.UsuarioController import usuario_controller
from controllers.UsuarioController import api as ns_usuario
from controllers.TarefaController import tarefa_controller
from controllers.TarefaController import api as ns_tarefa

app = Flask(__name__)

CORS(app)

api = Api(app
          , version="1.0"
          , title="Gerenciador de Tarefas"
          , description="Aplicação para gerenciar tarefas Devaria 2021"
          , doc='/docs')


#def register_blueprints():
#    app.register_blueprint(login_controller, url_prefix=config.API_BASE_URL)
#    app.register_blueprint(usuario_controller, url_prefix=config.API_BASE_URL)
#    app.register_blueprint(tarefa_controller, url_prefix=config.API_BASE_URL)
#    pass


def register_namespaces():
    api.add_namespace(ns_login, path=config.API_BASE_URL)
    api.add_namespace(ns_usuario, path=config.API_BASE_URL)
    api.add_namespace(ns_tarefa, path=config.API_BASE_URL)
    pass


if __name__ == '__main__':
    #register_blueprints()
    register_namespaces()
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)

