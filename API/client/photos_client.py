from API.client.base_client import BaseApiClient



class PhotosClient(BaseApiClient):

    def get_photo(self, photo_id: int):
        return self.session.get(self._url(f'/photos/{photo_id}'))


    def create_photo(self, albumid: int, title: str, url: str):
        payload = {'albumId': albumid, 'title': title, 'url': url}
        return self.session.post(self._url('/photos'), json = payload)


    def update_photo(self, photo_id: int, albumid: int, title: str, url: str):
        payload = {'albumId': albumid, 'title': title, 'url': url}
        return self.session.put(self._url(f'/photos/{photo_id}'), json=payload)

    def delete_photo(self, photo_id: int):
        return self.session.delete(self._url(f'/photos/{photo_id}'))