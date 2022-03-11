import pytest
from flaskr import create_app
from json import loads


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.mark.items
def test_item_aged_brie(client):
    response = client.get("/items/Aged%20Brie")
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    first_item = data[0]
    assert first_item['name'] == "Aged Brie", "No es el item correcto"
