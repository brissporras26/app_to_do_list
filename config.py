#configuracion  URL de la base de datos y la clave secreta

class Config:
    SECRET_KEY = 'mi_clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mi_base_de_datos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'app/static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
