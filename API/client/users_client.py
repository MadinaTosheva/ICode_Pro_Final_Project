from API.client.base_client import BaseApiClient


class UsersClient(BaseApiClient):

    def get_user(self, user_id: int ):
        return self.session.get(self._url(f'/users/{user_id}'))


    def create_user(self, name: str, username: str, email: str):
        payload = {"name": name, "username": username, "email": email}
        return self.session.post(self._url('/users'), json = payload)


    def update_user(self, user_id: int, name: str, username: str, email: str ):
        payload = {"name": name, "username": username, "email": email}
        return self.session.put(self._url(f'/users/{user_id}'), json = payload)


    def delete_user(self, user_id: int):
        return self.session.delete(self._url(f'/users/{user_id}'))

