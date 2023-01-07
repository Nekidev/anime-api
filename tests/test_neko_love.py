"""
Run tests for the NekoLoveAPI class

Usage:
    cd tests
    poetry run python -m pytest neko_love.py
"""
from anime_api.apis import NekoLoveAPI
from anime_api.apis.neko_love.obejcts import Image
from anime_api.apis.neko_love.types import ImageCategory


def test_get_random_image():
    """
    Test the get_random_image method
    """
    api = NekoLoveAPI()
    image = api.get_random_image(ImageCategory.SFW.NEKO)

    assert isinstance(image, Image)
    assert image.nsfw is False

    image = api.get_random_image(ImageCategory.NSFW.NEKO)

    assert isinstance(image, Image)
    assert image.nsfw is True
