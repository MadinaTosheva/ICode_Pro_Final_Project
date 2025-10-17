class TestUsers:

    def test_get_user(self, users_api):
        response = users_api.get_user(1)
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == 1
        assert 'name' in data
        assert 'username' in data
        assert 'email' in data


    def test_create_user(self, users_api):
        response = users_api.create_user('My name', 'My username', 'Myemail@gmail.com')
        assert response.status_code == 201
        data = response.json()
        assert data['name'] == 'My name'
        assert data['username'] == 'My username'
        assert data['email'] == 'Myemail@gmail.com'


    def test_update_user(self, users_api):
        response = users_api.update_user(2, 'My new name', 'My new username', 'MyNewemail@gmail.com')
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == 2
        assert data['name'] == "My new name"
        assert data['username'] == "My new username"
        assert data['email'] == "MyNewemail@gmail.com"




    def test_delete_user(self, users_api):
        response = users_api.delete_user(2)
        assert response.status_code == 200
        data = response.json()
        assert response.text == "{}" or response.text == ''

