import pytest
from flask import Flask
from backend.app.api.routes import api

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_world(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == {"message": "Hello, World!"}
