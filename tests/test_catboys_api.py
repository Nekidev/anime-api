"""
Run tests for the AnimuAPI class

Usage:
    Replace the api_token variable with your API token.

    cd tests
    poetry run python -m pytest test_catboys_api.py
"""
from anime_api.apis import CatboysAPI
from anime_api.apis.catboys import objects


def test_get_random_image():
    """
    Test the get_random_image method
    """
    api = CatboysAPI()
    image = api.get_random_image()
    assert isinstance(image, objects.Image)


def test_get_random_baka_gif():
    """
    Test the get_random_baka_gif method
    """
    api = CatboysAPI()
    gif = api.get_random_baka_gif()
    assert isinstance(gif, str)


def test_get_eight_ball():
    """
    Test the get_eight_ball method
    """
    api = CatboysAPI()
    eight_ball = api.get_eight_ball()
    assert isinstance(eight_ball, objects.EightBall)


def test_get_dice_roll():
    """
    Test the get_dice_roll method
    """

    api = CatboysAPI()
    dice_roll = api.get_dice_roll()
    assert isinstance(dice_roll, objects.DiceRoll)


def test_get_catboy_saying():
    """
    Test the get_catboy_saying method
    """

    api = CatboysAPI()
    catboy_saying = api.get_catboy_saying()
    assert isinstance(catboy_saying, str)
