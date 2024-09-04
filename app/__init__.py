from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuraciones de la aplicación

    # Importar y registrar rutas
    with app.app_context():

        
        from app.routes.home import home_bp
        from app.routes.user import user_bp
        from app.routes.tasks import task_bp
        from app.routes.auth import auth_bp

        
        app.register_blueprint(home_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(task_bp)
        app.register_blueprint(auth_bp)

    return app
