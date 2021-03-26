import pytest

from app import app


@pytest.fixture
def client(mocker):
    app.config["PRIVATE_API_KEY"] = "valid-key"
    client = app.test_client()
    with app.app_context():
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello world!"


def test_hello_name(client):
    response = client.get("/hello/Jose")
    assert response.status_code == 200
    assert response.data.decode() == "Hola Jose!"
