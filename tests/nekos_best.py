"""
Run tests for the NekosBest class
"""
from anime_api.apis import NekosBest
from anime_api.apis.nekos_best.objects import Image
from anime_api.apis.nekos_best.types import ImageCategory, ImageType


def test_get_random_images():
    """
    Tests the get_random_images method
    """
    api = NekosBest()
    images = api.get_random_images(ImageCategory.NEKO)
    assert isinstance(images, list)
    assert len(images) > 0
    assert isinstance(images[0], Image)


def test_search_images():
    """
    Tests the search_images method
    """
    api = NekosBest()
    images = api.search_images("neko", ImageCategory.NEKO, ImageType.IMAGE, 3)
    for image in images:
        assert isinstance(image, Image)
        assert not image.url.endswith(".gif")
