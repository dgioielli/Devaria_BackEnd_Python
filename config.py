import random
import string

API_PORT = 5000
API_HOST = "127.0.0.1"
API_BASE_URL = '/api'

DEBUG = True

#LOGIN_TESTE = "admin"
#SENHA_TESTE = "1234"

# Gera uma chave aleatória
gen = string.ascii_letters + string.digits + string.ascii_uppercase
SECRET_KEY = ''.join(random.choice(gen) for i in range(32))

#Configuração SQL
MYSQL_HOST='mysqlgerenciadortarefasdoug.cb5hlejo5meq.sa-east-1.rds.amazonaws.com'
MYSQL_PORT=3306
MYSQL_USER='DevariaUser'
MYSQL_PASS='Devaria2020'
MYSQL_DATABASE='dbGerenciadorTarefas4'

