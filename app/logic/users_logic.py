from database import database_manager


def get_profile(email):
    try:
        # Buscar perfil de usuario por email
        profile = database_manager.select('profiles', {'email': email})
        profile_list = list(profile)  # Convertir el cursor en una lista
        if not profile_list:
            return None
        return profile_list[0]
    except Exception as e:
        print(f"Error al obtener el perfil: {e}")
        raise

def create_profile(name, email):
    try:
        # Verificar si el perfil ya existe
        existing_profile = get_profile(email)
        if existing_profile:
            return False  # El perfil ya existe

        # Crear nuevo perfil
        profile_data = {'name': name, 'email': email}
        profile_id = database_manager.insert('profiles', profile_data)
        return profile_id
    except Exception as e:
        print(f"Error al crear el perfil: {e}")
        raise

def delete_profile(email):
    try:
        # Verificar si el perfil existe
        existing_profile = get_profile(email)
        if not existing_profile:
            return False  # El perfil no existe

        # Eliminar perfil
        result = database_manager.delete('profiles', {'email': email})
        return result > 0
    except Exception as e:
        print(f"Error al eliminar el perfil: {e}")
        raise

def update_profile(email, new_email):
    try:
        # Verificar si el perfil existe
        existing_profile = get_profile(email)
        if not existing_profile:
            return False  # El perfil no existe

        # Actualizar perfil
        update_result = database_manager.update('profiles', {'email': email}, {'email': new_email})
        return update_result > 0
    except Exception as e:
        print(f"Error al actualizar el perfil: {e}")
        raise
