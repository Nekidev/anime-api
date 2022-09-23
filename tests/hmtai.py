"""
Run tests for the HmtaiAPI class.

Usage:
    cd tests
    poetry run python -m pytest hmtai.py
"""
from anime_api.apis import HmtaiAPI
from anime_api.apis.hmtai.objects import Image
from anime_api.apis.hmtai.types import ImageCategory


def test_get_random_image():
    """
    Test the get_random_image method
    """

    api = HmtaiAPI()
    image = api.get_random_image(ImageCategory.SFW.KISS)
    assert isinstance(image, Image)
    assert not image.nsfw
