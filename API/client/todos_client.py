from API.client.base_client import BaseApiClient


class TodosClient(BaseApiClient):

    def get_todo(self, todo_id: int):
        return self.session.get(self._url(f'/todos/{todo_id}'))

    def create_todo(self, userid: int, title: str, completed: bool):
        payload = {"userId": userid, "title": title, "completed": completed}
        return self.session.post(self._url('/todos'), json=payload)

    def update_todo(self, todo_id: int, userid: int, title: str, completed: bool):
        payload = {"userId": userid, "title": title, "completed": completed}
        return self.session.put(self._url(f'/todos/{todo_id}'), json=payload)

    def delete_todo(self, todo_id: int):
        return self.session.delete(self._url(f'/todos/{todo_id}'))