from API.client.base_client import BaseApiClient


class PostsClient(BaseApiClient):


    def get_post(self, post_id: int):
        return self.session.get(self._url(f'/posts/{post_id}'))


    def create_post(self, title: str, body: str, user_id: int):
        payload = {"title": title, "body": body, "user_id": user_id}
        return self.session.post(self._url('/posts'), json = payload)


    def update_post(self, post_id: int, title: str, body: str, user_id: int):
        payload  = {"title": title, "body": body, "user_id": user_id}
        return self.session.put(self._url(f'/posts/{post_id}'), json = payload)


    def delete_post(self, post_id: int):
        return self.session.delete(self._url(f'/posts/{post_id}'))



