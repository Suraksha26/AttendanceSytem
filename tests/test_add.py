def test_add_user(client):
    response = client.post('/add', data={'newusername': 'Suraksha', 'newuserid': '123'})
    assert response.status_code == 200
    assert b'User added successfully' in response.data