from werkzeug.security import check_password_hash
from database import database_manager

def authenticate_user(email, password):
    # Nombre de la base de datos y la colección
    db_name = "NombreDeTuBaseDeDatos"
    collection_name = "users"

    # Consulta para obtener el usuario por email
    query = {"email": email}

    # Obtén el usuario de la base de datos
    user = database_manager.select(db_name=db_name, collection_name=collection_name, query=query).first()  # Usar `.first()` para obtener el primer documento

    # Verifica la contraseña
    if user and check_password_hash(user['password'], password):
        return True
    return False

def create_user(email, password):
    # Implementación para crear un usuario
    pass
