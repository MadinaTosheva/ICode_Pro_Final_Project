from API.client.base_client import BaseApiClient


class CommentsClient (BaseApiClient):

    def get_comment(self, comment_id: int):
        return self.session.get(self._url(f'/comments/{comment_id}'))


    def create_comment(self, post_id: int, name: str, body: str):
        payload = {'postId': post_id, 'name': name, 'body': body}
        return self.session.post(self._url('/comments'), json = payload)


    def update_comment(self, comment_id: int, post_id: int, name: str, body: str):
        payload = {'postId': post_id, 'name': name, 'body': body}
        return self.session.put(self._url(f'/comments/{comment_id}'), json = payload)


    def delete_comment(self, comment_id: int):
        return self.session.delete(self._url(f'/comments/{comment_id}'))
