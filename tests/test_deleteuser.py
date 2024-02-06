def test_delete_user(client):
    response = client.get('/deleteuser?user=testuser')
    assert response.status_code == 200
    assert b'User deleted successfully' in response.data