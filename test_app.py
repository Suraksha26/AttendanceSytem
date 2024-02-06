import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200


def test_listusers_route(client):
    response = client.get('/listusers')
    assert response.status_code == 200


def test_start_route(client):
    response = client.get('/start')
    assert response.status_code == 200


def test_add_route(client):
    response = client.post('/add', data={'newusername': 'TestUser', 'newuserid': '123'})
    assert response.status_code == 200


def test_deleteuser_route(client):
    response = client.get('/deleteuser?user=TestUser_123')
    assert response.status_code == 200
