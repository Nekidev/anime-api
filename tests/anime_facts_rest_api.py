"""
Run tests for the AnimeFactsRestAPI class.

Usage:
    cd tests
    poetry run python -m pytest anime_facts_rest_api.py
"""

import typing

from anime_api.apis.anime_facts_rest_api import AnimeFactsRestAPI
from anime_api.apis.anime_facts_rest_api.objects import Anime, Fact


def test_get_animes():
    """
    Test the get_animes method. Should return a list of animes.
    """
    animes: typing.List[Anime] = AnimeFactsRestAPI().get_animes()

    assert isinstance(
        animes, list
    ), "The return type of get_animes() is not a list."
    assert len(animes) > 0, "The list of animes is empty."
    assert isinstance(
        animes[0], Anime
    ), "The list of animes does not contain objects.Anime objects."


def test_get_anime_facts():
    """
    Test the get_anime_facts method. Should return a list of facts.
    """
    facts: typing.List[Fact] = AnimeFactsRestAPI().get_anime_facts(anime_name="naruto")

    assert isinstance(
        facts, list
    ), "The return type of get_anime_facts() is not a list."
    assert len(facts) > 0, "The list of facts is empty."
    assert isinstance(
        facts[0], Fact
    ), "The list of facts does not contain objects.Fact objects."

def test_get_fact():
    """
    Test the get_fact method. Should return a single fact.
    """
    fact: Fact = AnimeFactsRestAPI().get_fact(anime_name="naruto", fact_id=1)

    assert isinstance(
        fact, Fact
    ), "The return type of get_fact() is not a objects.Fact object."
