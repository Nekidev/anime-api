"""
Run tests for the KyokoAPI class

Usage:
    cd tests
    poetry run python -m pytest kyoko.py
"""
from anime_api.apis import KyokoAPI
from anime_api.apis.kyoko.objects import Quote, Image


def test_get_random_quote():
    """
    Test that the API returns a quote.
    """
    api = KyokoAPI()
    quote = api.get_random_quote()
    assert quote.quote
    assert quote.anime
    assert quote.character
    assert quote.id
    assert isinstance(quote, Quote)


def test_get_random_slap():
    """
    Test that the API returns a slap image.
    """
    api = KyokoAPI()
    image = api.get_random_slap()
    assert image.url
    assert isinstance(image, Image)


def test_get_random_kiss():
    """
    Test that the API returns a kiss image.
    """
    api = KyokoAPI()
    image = api.get_random_kiss()
    assert image.url
    assert isinstance(image, Image)


def test_get_random_hug():
    """
    Test that the API returns a hug image.
    """
    api = KyokoAPI()
    image = api.get_random_hug()
    assert image.url
    assert isinstance(image, Image)
