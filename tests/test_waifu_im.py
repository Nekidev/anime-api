"""
Run tests for the WaifuPicsAPI class.

Usage:
    cd tests
    poetry run python -m pytest waifu_im.py
"""
import typing

from anime_api.apis import WaifuImAPI
from anime_api.apis.waifu_im.types import ImageTag
from anime_api.apis.waifu_im.objects import Image


def test_get_random_image():
    """
    Test the get_random_image method
    """
    api = WaifuImAPI()
    image = api.get_random_image()

    assert isinstance(image, Image)
    assert image.url
    assert image.tags
    assert isinstance(image.tags[0], typing.Union[ImageTag.SFW, ImageTag.NSFW])


def test_get_many_random_images():
    """
    Test the get_many_random_images method
    """
    api = WaifuImAPI()
    images = api.get_many_random_images()

    assert isinstance(images, list)
    assert len(images) == 30
    for image in images:
        assert isinstance(image, Image)
        assert image.url
        assert image.tags
        assert isinstance(image.tags[0], typing.Union[ImageTag.SFW, ImageTag.NSFW])
