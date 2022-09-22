"""
Run tests for the WaifuPicsAPI class.

Usage:
    cd tests
    poetry run python -m pytest waifu_pics.py
"""
from anime_api.apis import WaifuPicsAPI
from anime_api.apis.waifu_pics.types import ImageCategory
from anime_api.apis.waifu_pics.objects import Image


def test_get_image():
    """
    Test the get_image method
    """
    image = WaifuPicsAPI().get_image(ImageCategory.SFW.WAIFU)
    assert isinstance(image, Image)
    assert isinstance(image.url, str)
    assert isinstance(image.nsfw, bool) and not image.nsfw


def test_get_many_images():
    """
    Test the get_many_images method
    """
    images = WaifuPicsAPI().get_many_images(ImageCategory.SFW.WAIFU)
    assert isinstance(images, list)
    assert len(images) == 30
    for image in images:
        assert isinstance(image, Image)
        assert isinstance(image.url, str)
        assert isinstance(image.nsfw, bool) and not image.nsfw

def test_get_many_images_with_exclude():
    """
    Test the get_many_images method with exclude filter
    """
    image_url = "https://i.waifu.pics/tLc5RfN.png" # Cute image btw
    images = WaifuPicsAPI().get_many_images(ImageCategory.SFW.WAIFU, exclude=[image_url])
    assert isinstance(images, list)
    assert len(images) == 30
    for image in images:
        assert isinstance(image, Image)
        assert isinstance(image.url, str)
        assert isinstance(image.nsfw, bool) and not image.nsfw
        assert image.url != image_url
