import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert b'Home Page' in response.data
    assert response.status_code == 200

def test_list_users_page(client):
    response = client.get('/listusers')
    assert b'List of Users' in response.data
    assert response.status_code == 200

def test_delete_user(client):
    response = client.get('/deleteuser?user=test_user')
    assert response.status_code == 200

def test_start_page(client):
    response = client.get('/start')
    assert response.status_code == 200

def test_add_user(client):
    response = client.post('/add', data={'newusername': 'test_user', 'newuserid': '123'})
    assert response.status_code == 200
