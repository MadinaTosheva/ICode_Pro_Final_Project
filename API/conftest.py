import pytest

from API.client.comments_client import CommentsClient
from API.client.photos_client import PhotosClient
from API.client.post_client import PostsClient
from API.client.todos_client import TodosClient
from API.client.users_client import UsersClient

API_BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def posts_api():
    return PostsClient(API_BASE_URL)


@pytest.fixture(scope="session")
def users_api():
    return UsersClient(API_BASE_URL)


@pytest.fixture(scope="session")
def comments_api():
    return CommentsClient(API_BASE_URL)


@pytest.fixture(scope="session")
def photos_api():
    return PhotosClient(API_BASE_URL)


@pytest.fixture(scope="session")
def todos_api():
    return TodosClient(API_BASE_URL)






