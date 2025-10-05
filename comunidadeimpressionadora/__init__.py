from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '62ab39f001232385bb3064674a72c76b' #Chave que proteje a sessão do usuário

# VARIAVEL DE AMBIENTE: indica se o banco esta local ou remoto
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar a página.'
login_manager.login_message_category = 'alert-info'

# Avalia e cria o banco de dados no servidor remoto se não existir
from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspect = sqlalchemy.inspect(engine)

if not inspect.has_table("usuario"):
    with app.app_context():
        #database.drop_all()
        database.create_all()
        print("Base de dados criada com sucesso.")
else:
    print("Base de dados existente")

# A importação do routes deve ser feita aqui
from comunidadeimpressionadora import routes
