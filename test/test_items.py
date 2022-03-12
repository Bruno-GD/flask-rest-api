import pytest
from flaskr import create_app
from json import loads
from flask import g


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


@pytest.mark.items
def test_item_quality(client):
    response = client.get("/items/quality/50")
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    first_item = data[0]
    assert first_item['quality'] == 50, "'quality' no es correcto"


@pytest.mark.items
def test_item_sell_in(client):
    response = client.get("/items/sell_in/3")
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    first_item = data[0]
    assert first_item['sell_in'] == 3, "'sell_in' no es correcto"


@pytest.mark.items
def test_new_item(client):
    app = client.application
    with app.app_context():
        response = client.post("/items", data={"name": "Test", "quality": 1, "sell_in": 1})
        assert response.status_code == 202
        db = g.get('session')
        db.rollback()
