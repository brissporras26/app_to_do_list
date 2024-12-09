import pytest
from app.logic.users_logic import register_user_logic, login_user_logic

from database.database_manager import database_manager


from werkzeug.security import check_password_hash

@pytest.fixture
def user_fixture():
    email = "testuser@example.com"
    password = "password123"
    # Llamamos al método de registro
    register_user_logic(email, password)
    return email, password

def test_login_user_valid_credentials(user_fixture):
    email, password = user_fixture
    # Verificamos si el login con credenciales válidas es exitoso
    result = login_user_logic(email, password)
    assert result is True

def test_login_user_invalid_credentials():
    # Probamos un login con credenciales inválidas
    email = "invaliduser@example.com"
    password = "wrongpassword"
    result = login_user_logic(email, password)
    assert result is False

def test_login_user_without_password(user_fixture):
    email, password = user_fixture
    # Probamos un login donde el usuario no tiene contraseña (registro via Auth0 sin contraseña)
    user_list = list(database_manager.select(
        db_name=None,
        collection_name="users",
        query={"email": email}
    ))
    user_list[0]['password'] = None  # Simulamos un caso donde no hay contraseña
    result = login_user_logic(email, password)
    assert result is False  # Aseguramos que la función devuelva False cuando no haya contraseña
