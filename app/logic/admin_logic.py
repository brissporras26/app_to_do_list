from database import database_manager

def get_all_users():
    """
    Obtiene todos los usuarios de la colección 'users'.
    :return: Lista de documentos de usuarios.
    """
    try:
        # Usar db para seleccionar todos los usuarios
        users = database_manager.select('users', {})
        return list(users)  # Convertir el cursor en una lista
    except Exception as e:
        print(f"Error al obtener todos los usuarios: {e}")
        raise

def get_user_by_id(user_id):
    """
    Obtiene un usuario por su ID.
    :param user_id: ID del usuario a buscar.
    :return: Documento del usuario si se encuentra, de lo contrario None.
    """
    try:
        # Usar db para buscar el usuario por ID
        user = database_manager.select('users', {'_id': user_id})
        user_list = list(user)  # Convertir el cursor en una lista
        if not user_list:
            return None
        return user_list[0]
    except Exception as e:
        print(f"Error al obtener el usuario por ID: {e}")
        raise

def update_user(user_id, update_data):
    """
    Actualiza la información de un usuario.
    :param user_id: ID del usuario a actualizar.
    :param update_data: Datos a actualizar.
    :return: Número de documentos modificados.
    """
    try:
        # Usar db para actualizar el usuario
        result = database_manager.update('users', {'_id': user_id}, update_data)
        return result
    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")
        raise

def delete_user(user_id):
    """
    Elimina un usuario de la colección 'users'.
    :param user_id: ID del usuario a eliminar.
    :return: Número de documentos eliminados.
    """
    try:
        # Usar db para eliminar el usuario
        result = database_manager.delete('users', {'_id': user_id})
        return result
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        raise
