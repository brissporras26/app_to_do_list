import pytest
from app import create_app  # Asegúrate de que create_app esté correctamente importado desde tu aplicación

# Usar 'module' o 'session' para asegurar que la fixture 'app' se cree una sola vez
@pytest.fixture(scope="module")
def app():
    """Fixture que crea la instancia de la aplicación para pruebas"""
    app = create_app()
    app.config['TESTING'] = True  # Activa el modo de pruebas
    app.config['SECRET_KEY'] = 'test-secret'  # Define una clave secreta para las pruebas
    yield app  # Proporciona la instancia de la aplicación para los tests
    # Aquí puedes agregar cualquier limpieza si es necesario después de la prueba

# Proporciona un cliente de prueba para hacer peticiones a la aplicación
@pytest.fixture(scope="module")
def client(app):
    """Fixture que proporciona un cliente de pruebas para hacer peticiones a la aplicación"""
    return app.test_client()

# Fixture para obtener un runner de comandos de Flask (opcional)
@pytest.fixture(scope="module")
def runner(app):
    """Fixture para obtener el runner de comandos de Flask"""
    return app.test_cli_runner()
