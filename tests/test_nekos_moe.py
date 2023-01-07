"""
Run tests for the NekosMoeAPI class

Usage:
    cd tests
    poetry run python -m pytest nekos_moe.py
"""
from anime_api.apis import NekosMoeAPI
from anime_api.apis.nekos_moe.objects import Image, User


USERNAME = "YOUR_USERNAME_HERE"
PASSWORD = "YOUR_PASSWORD_HERE"


def test_get_random_image():
    """
    Test that the API returns an image.
    """
    api = NekosMoeAPI(USERNAME, PASSWORD)
    images = api.get_random_images(2)
    assert len(images) == 2
    for image in images:
        assert isinstance(image, Image)
        assert image.url
        assert image.created_at

def test_get_image():
    """
    Test that the API returns an image.
    """
    api = NekosMoeAPI(USERNAME, PASSWORD)
    image = api.get_image("Hy70M3kig")
    assert isinstance(image, Image)
    assert image.url

def test_get_user():
    """
    Test that the API returns a user.
    """
    api = NekosMoeAPI(USERNAME, PASSWORD)
    user = api.get_user()
    assert isinstance(user, User)
    assert user.username
    assert user.id
    assert user.likes
    for image in user.likes:
        assert isinstance(image, Image)
        assert image.url
        assert image.created_at

def test_get_user_by_id():
    """
    Test that the API returns a user.
    """
    api = NekosMoeAPI(USERNAME, PASSWORD)
    user = api.get_user("E-ncJUU6T")
    assert isinstance(user, User)
    assert user.username
    assert user.id

def test_search_users():
    """
    Test that the API returns a list of users.
    """
    api = NekosMoeAPI(USERNAME, PASSWORD)
    users = api.search_users(query="nekii")
    for user in users:
        assert isinstance(user, User)
        assert user.username
        assert user.id

def test_search_images():
    """
    Test that the API returns images.
    """
    api = NekosMoeAPI(USERNAME, PASSWORD)
    images = api.search_images(tags=["cat"])
    for image in images:
        assert isinstance(image, Image)
        assert image.url
        assert image.created_at
