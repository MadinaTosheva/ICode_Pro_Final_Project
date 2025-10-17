import pytest



class TestPosts:

   def test_get_post(self, posts_api):
    response = posts_api.get_post(1)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert 'title' in data
    assert 'body' in data
    assert 'userId' in data



   def test_create_post(self, posts_api):
    response = posts_api.create_post("My title", "My body", 2)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == "My title"
    assert data['body'] == "My body"
    assert data['user_id'] == 2


   def test_update_post(self, posts_api):
    response = posts_api.update_post(1, "My updated title", "My updated body", 2)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == "My updated title"
    assert data['body'] == "My updated body"
    assert data['user_id'] == 2


   def test_delete_post(self, posts_api):
    response = posts_api.delete_post(1)
    assert response.status_code == 200
    assert response.text == "{}" or response.text == ''











