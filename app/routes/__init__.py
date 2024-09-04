from flask import Blueprint

#Definir los Blueprints
admin = Blueprint('home', __name__)
auth = Blueprint('auth', __name__)
user = Blueprint('user', __name__)
task = Blueprint('task', __name__)


