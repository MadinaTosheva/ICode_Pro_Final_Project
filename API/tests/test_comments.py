import pytest


class TestComments:

    def test_get_comment(self, comments_api):
        response = comments_api.get_comment(5)
        assert response.status_code == 200
        data = response.json()
        assert 'name' in data
        assert 'body' in data


    def test_create_comment(self, comments_api):
        response = comments_api.create_comment(6, "Madina", "I am hungry")
        assert response.status_code == 201
        data = response.json()
        assert data['postId'] == 6
        assert data['name'] == "Madina"
        assert data['body'] == "I am hungry"


    def test_update_comment(self, comments_api):
        response = comments_api.update_comment(2, 22, "Maddie", "Let's have a coffee")
        assert response.status_code == 200
        data = response.json()
        assert data['postId'] == 22
        assert data['name'] == "Maddie"
        assert data['body'] == "Let's have a coffee"


    def test_delete_comment(self, comments_api):
        response = comments_api.delete_comment(2)
        assert response.status_code == 200
        assert response.text == '{}' or response.text == ''





