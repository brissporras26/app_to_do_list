from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    load_dotenv()
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    @app.before_request
    def before_request():
        if request.method == 'POST' and '_method' in request.form:
            request.method = request.form['_method'].upper()
    
    # Importar y registrar rutas
    with app.app_context():

        from app.routes.home import home_bp
        from app.routes.user import user_bp
        from app.routes.tasks import task_bp
        from app.routes.index import index_bp
        
        app.register_blueprint(home_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(task_bp)
        app.register_blueprint(index_bp)

    return app
