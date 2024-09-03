from flask import Blueprint

#Definir los Blueprints
home_bp = Blueprint('home', __name__)
auth_bp = Blueprint('auth', __name__)
user_bp = Blueprint('user', __name__)
task_bp = Blueprint('task', __name__)

#importar las rutas para que se registren en los Blueprints
from app.routes import users, tasks, auth
