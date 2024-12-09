import pytest
from app import create_app

@pytest.fixture(scope="module")
def app():
    """Create application for testing"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret'
    return app

@pytest.fixture(scope="module")
def client(app):
    """Create client for testing"""
    return app.test_client()

@pytest.fixture(scope="module")
def runner(app):
    """Create runner for testing"""
    return app.test_cli_runner()