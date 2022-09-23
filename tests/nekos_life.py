"""
Run tests for the NekosLifeAPI class.

Usage:
    cd tests
    poetry run python3 -m pytest nekos_life.py
"""
from anime_api.apis import NekosLifeAPI
from anime_api.apis.nekos_life.objects import EightBall, Fact, Image
from anime_api.apis.nekos_life.types import ImageType


def test_get_eight_ball():
    """
    Test the get_eight_ball method.
    """
    api = NekosLifeAPI()
    eight_ball = api.get_eight_ball()

    assert isinstance(eight_ball, EightBall)
    assert isinstance(eight_ball.answer, str)
    assert isinstance(eight_ball.image, Image)
    assert isinstance(eight_ball.image.url, str)


def test_get_random_cat_emoji():
    """
    Test the get_random_cat_emoji method.
    """
    api = NekosLifeAPI()
    cat_emoji = api.get_random_cat_emoji()

    assert isinstance(cat_emoji, str)


def test_get_random_fact():
    """
    Test the get_random_fact method.
    """
    api = NekosLifeAPI()
    fact = api.get_random_fact()

    assert isinstance(fact, Fact)
    assert isinstance(fact.fact, str)


def test_get_random_name():
    """
    Test the get_random_name method.
    """
    api = NekosLifeAPI()
    name = api.get_random_name()

    assert isinstance(name, str)


def test_get_random_image():
    """
    Test the get_random_image method.
    """
    api = NekosLifeAPI()
    image = api.get_random_image(ImageType.SMUG)

    assert isinstance(image, Image)
    assert isinstance(image.url, str)


def test_owoify():
    """
    Test the owoify method.
    """
    api = NekosLifeAPI()
    owoified = api.owoify("hello world")

    assert isinstance(owoified, str)
    assert owoified == "hewwo wowwd"


def test_spoiler():
    """
    Test the spoiler method.
    """
    api = NekosLifeAPI()
    spoilered = api.spoiler("hello world")

    assert isinstance(spoilered, str)
    assert spoilered == "||hello world||"


def test_get_random_why():
    """
    Test the get_random_why method.
    """
    api = NekosLifeAPI()
    why = api.get_random_why()

    assert isinstance(why, str)
    assert why.endswith('?')
