import pytest
from json import loads
from flask import g
from flaskr.repository.types.Item import Item


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
    response = client.post("/items", data={"name": "Test", "quality": 1, "sell_in": 1})
    assert response.status_code == 202

    # obtenemos la sesion
    db = g.get('session')
    # buscamos el item insertado antes en el post
    item = db.query(Item).filter_by(name="Test").one_or_none()
    assert item is not None, "No está el item"


@pytest.mark.items
def test_update_quality(client):
    db = g.get("session")
    old_item_quality = db.query(Item).filter_by(name="+5 Dexterity Vest").first().quality
    assert client.get("/update_quality").status_code == 202, "Status code erroneo"
    assert 'shop' in g, 'No existe shop en el contexto'
    quality_first_item = g.shop.items[0].quality
    assert client.get("/update_quality").status_code == 202, "Status code erroneo"
    assert quality_first_item != g.shop.items[0].quality, "No ha cambiado la calidad"
    updated_item_quality = db.query(Item).filter_by(name="+5 Dexterity Vest").first().quality
    assert old_item_quality != updated_item_quality, "La calidad no ha cambiado"


@pytest.mark.items
def test_delete_item(client):
    assert client.delete("/items/name/Aged%20Brie/delete").status_code == 202, "Status code erroneo"
    assert 'session' in g, "No hay db"
    db = g.get('session')
    assert db.query(Item).filter_by(name="Aged Brie").one_or_none() is None, "No se ha borrado"
