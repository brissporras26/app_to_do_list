"""from database import database_manager


def get_profile_logic(email):
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

def create_profile_logic(name, email):
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

"""