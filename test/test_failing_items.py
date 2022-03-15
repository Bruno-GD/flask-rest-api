import pytest


@pytest.mark.failing_items
def test_filters_with_str(client):
    assert client.get('/items/quality/a').status_code == 404, "Respuesta no esperada"
    assert client.get('/items/sell_in/a').status_code == 404, "Respuesta no esperada"


@pytest.mark.failing_items
def test_insert(client):
    assert client.post('/items', data={}).status_code == 400, "Respuesta no esperada"
