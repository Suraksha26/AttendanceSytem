def test_list_users_page(client):
    response = client.get('/listusers')
    assert response.status_code == 200
    assert b'List of Users' in response.data