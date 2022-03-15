import pytest
from json import loads
from flask import g


@pytest.mark.items
def test_item_aged_brie(client):
    response = client.get("/items/name/Aged%20Brie")
    assert response.status_code == 200, "Respuesta no esperada: %s" % response.data
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    first_item = data[0]
    assert first_item['name'] == "Aged Brie", "No es el item correcto"


@pytest.mark.items
def test_item_quality(client):
    response = client.get("/items/quality/80")
    assert response.status_code == 200, "Respuesta no esperada: %s" % response.data
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    first_item = data[0]
    assert first_item['quality'] == 80, "'quality' no es correcto"


@pytest.mark.items
def test_item_sell_in(client):
    response = client.get("/items/sell_in/2")
    assert response.status_code == 200, "Respuesta no esperada: %s" % response.data
    data = loads(response.data)
    assert len(data) > 0, "Debería haber minimo 1 item"
    first_item = data[0]
    assert first_item['sell_in'] == 2, "'sell_in' no es correcto"


@pytest.mark.items
def test_new_item(client):
    app = client.application
    with app.app_context():
        response = client.post("/items", data={"name": "Test", "quality": 1, "sell_in": 1})
        assert response.status_code == 202

        # obtenemos la sesion
        db = g.get('session')
        # importamos el type Item para sqlalchemy
        from flaskr.repository.types.Item import Item
        # buscamos el item insertado antes en el post
        item = db.query(Item).filter_by(name="Test").one_or_none()
        assert item is not None, "No está el item"
        # borramos los cambios
        db.rollback()


@pytest.mark.items
def test_update_quality(client):
    app = client.application
    with app.app_context():
        assert client.get("/update_quality").status_code == 200, "Status code erroneo"
        assert 'shop' in g, 'No existe shop en el contexto'
        quality_first_item = g.shop.items[0].quality
        assert client.get("/update_quality").status_code == 200, "Status code erroneo"
        assert quality_first_item != g.shop.items[0].quality, "No ha cambiado la calidad"

        db = g.get('session')
        db.rollback()
