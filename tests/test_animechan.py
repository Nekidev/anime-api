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

    quote = AnimechanAPI().get_random_quote(anime_title="naruto")

    assert isinstance(quote, Quote), "The return type of get_quote() is not a Quote."
    assert (
        quote.anime.lower() == "naruto"
    ), "The returned quote is not from the selected anime."

    quote = AnimechanAPI().get_random_quote(character_name="naruto uzumaki")

    assert isinstance(quote, Quote), "The return type of get_quote() is not a Quote."
    assert (
        quote.character.lower() == "naruto uzumaki"
    ), "The returned quote is not from the selected character."


def test_get_many_random_quotes():
    """
    Test the get_many_random_quotes method. Should return a list of quotes.
    """
    quotes = AnimechanAPI().get_many_random_quotes()

    assert isinstance(
        quotes, list
    ), "The return type of get_many_random_quotes() is not a list."
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
