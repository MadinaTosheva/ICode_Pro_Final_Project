import pytest


class TestPhotos:

    def test_get_photo(self, photos_api):
        response = photos_api.get_photo(1)
        assert  response.status_code == 200
        data = response.json()
        assert data['id'] == 1
        assert 'title' in data
        assert 'url' in data


    def test_create_photo(self, photos_api):
        response =  photos_api.create_photo(2, 'Billie Eilish', 'https.billie.com')
        assert response.status_code == 201
        data = response.json()
        assert data['albumId'] == 2
        assert data['title'] == 'Billie Eilish'
        assert data['url'] == 'https.billie.com'


    def test_update_photo(self, photos_api):
        response = photos_api.update_photo(1, 1, 'Taylor Swift', 'https.taylor.com' )
        assert response.status_code == 200
        data = response.json()
        assert data['albumId'] == 1
        assert data['title'] == 'Taylor Swift'
        assert data['url'] == 'https.taylor.com'


    def test_delete_photo(self, photos_api):
        response = photos_api.delete_photo(1)
        assert response.status_code == 200
        assert response.text ==  '{}' or response.text == ''



