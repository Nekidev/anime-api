"""
Run tests for the AnimuAPI class

Usage:
    Replace the api_token variable with your API token.

    cd tests
    poetry run python -m pytest animu.py
"""
import time

from anime_api.apis import AnimuAPI
from anime_api.apis.animu import types, objects, operators


api_token = "YOUR_API_TOKEN_HERE"


def test_get_random_image():
    """
    Test the ger_random_image method
    """
    api = AnimuAPI(api_token)
    image = api.get_random_image(types.ImageType.PAT)
    assert isinstance(image, objects.Image)
    time.sleep(1)


def test_get_random_quote():
    """
    Test the get_random_quote method
    """
    api = AnimuAPI(api_token)
    quote = api.get_random_quote()
    assert isinstance(quote, objects.Quote)
    assert quote.anime
    assert quote.character
    assert quote.quote
    assert quote.id
    time.sleep(1)


def test_get_random_waifu():
    """
    Test the get_random_waifu method
    """
    api = AnimuAPI(api_token)
    waifu = api.get_random_waifu()
    assert isinstance(waifu, objects.Waifu)
    assert waifu.name
    assert waifu.from_
    assert waifu.statistics
    assert waifu.images
    time.sleep(1)


def test_get_random_fact():
    """
    Test the get_random_fact method
    """
    api = AnimuAPI(api_token)
    fact = api.get_random_fact()
    assert isinstance(fact, objects.Fact)
    assert fact.fact
    time.sleep(1)


def test_generate_random_password():
    """
    Test the generate_random_password method
    """
    api = AnimuAPI(api_token)
    password = api.generate_random_password()
    assert isinstance(password, str)
    time.sleep(1)
