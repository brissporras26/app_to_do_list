
from database.database_manager import  database_manager


def add_user_logic(email_user, password_user):
    
    user_data = {
        'email': email_user,
        'password': password_user
    }

    collection_name = 'users'
    inserted_user = database_manager.insert(db_name=None, collection_name=collection_name,data= user_data)
    # Imprimir para verificar la inserción
    print(f"Inserted user: {inserted_user}")
    return inserted_user


