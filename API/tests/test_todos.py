import pytest



class TestTodos:

    def test_get_todo(self, todos_api):
        response = todos_api.get_todo(1)
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == 1
        assert 'title' in data
        assert 'completed' in data
        assert 'userId' in data

    def test_create_todo(self, todos_api):
        response = todos_api.create_todo(2, "My todo list", True)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == "My todo list"
        assert data['completed'] == True
        assert data['userId'] == 2

    def test_update_todo(self, todos_api):
        response = todos_api.update_todo(1, 2, "Need to add more todos", False)
        assert response.status_code == 200
        data = response.json()
        assert data['title'] == "Need to add more todos"
        assert data['completed'] == False
        assert data['userId'] == 2

    def test_delete_todo(self, todos_api):
        response = todos_api.delete_todo(1)
        assert response.status_code == 200
        assert response.text == "{}" or response.text == ''