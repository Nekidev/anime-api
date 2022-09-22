"""
Run tests for the AnimechanAPI class.

Usage:
    cd tests
    poetry run python -m pytest animechan.py
"""
from anime_api.apis.animechan import AnimechanAPI
from anime_api.apis.animechan.objects import Quote


def test_get_quote():
    """
    Test the get_quote method. Should return a single quote.
    """
    quote = AnimechanAPI().get_random_quote()

    assert isinstance(quote, Quote), "The return type of get_quote() is not a Quote."


def test_get_10_random_quotes():
    """
    Test the get_10_random_quotes method. Should return a list of quotes.
    """
    quotes = AnimechanAPI().get_10_random_quotes()

    assert isinstance(
        quotes, list
    ), "The return type of get_10_random_quotes() is not a list."
    assert len(quotes) > 0, "The list of quotes is empty."
    for quote in quotes:
        assert isinstance(
            quote, Quote
        ), "The list of quotes does not contain Quote objects."


def test_search_quote_by_anime_title():
    """
    Test the search_quote_by_anime_title method. Should return a list of quotes.
    """
    quotes = AnimechanAPI().search_by_anime_title("Naruto")

    assert isinstance(
        quotes, list
    ), "The return type of search_quote_by_anime_title() is not a list."
    assert len(quotes) > 0, "The list of quotes is empty."
    for quote in quotes:
        assert isinstance(
            quote, Quote
        ), "The list of quotes does not contain Quote objects."


def test_search_quote_by_character_name():
    """
    Test the search_quote_by_character_name method. Should return a list of quotes.
    """
    quotes = AnimechanAPI().search_by_character_name("Naruto")

    assert isinstance(
        quotes, list
    ), "The return type of search_quote_by_character_name() is not a list."
    assert len(quotes) > 0, "The list of quotes is empty."


def test_get_animes():
    """
    Test the get_animes method. Should return a list of anime titles.
    """
    animes = AnimechanAPI().get_animes()

    assert isinstance(animes, list), "The return type of get_animes() is not a list."
    assert len(animes) > 0, "The list of animes is empty."
