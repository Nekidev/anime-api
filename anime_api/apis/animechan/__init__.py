"""
Base module for the Animechan API. The documentation is available at
https://animechan.vercel.app/guide
"""
from urllib.parse import quote_plus

import typing
import requests

from anime_api import exceptions
from anime_api.apis.animechan.objects import Quote


class AnimechanAPI:
    """
    Docs: https://animechan.vercel.app/guide
    """

    endpoint = "https://animechan.vercel.app/api"

    def __init__(self, endpoint: typing.Optional[str] = None):
        self.endpoint = endpoint or self.endpoint

    def get_random_quote(
        self,
        anime_title: typing.Optional[str] = None,
        character_name: typing.Optional[str] = None,
    ) -> Quote:
        """
        Get a random quote from the API.
        """
        response = requests.get(
            f"{self.endpoint}/random"
            + (
                "/character?name=" + quote_plus(character_name)
                if character_name
                else "/anime?title=" + quote_plus(anime_title)
                if anime_title
                else ""
            ),
            timeout=5
        )

        AnimechanAPI._check_response_code(response.status_code)

        return Quote(**response.json())

    def get_many_random_quotes(self) -> typing.List[Quote]:
        """
        Get 10 random quotes from the API.
        """
        response = requests.get(f"{self.endpoint}/quotes")

        AnimechanAPI._check_response_code(response.status_code)

        return [Quote(**quote) for quote in response.json()]

    def search_by_anime_title(
        self, anime_title: str, page: int = 1
    ) -> typing.List[Quote]:
        """
        Return a list of quotes from the given anime.
        """
        response = requests.get(
            f"{self.endpoint}/quotes/anime", params={"title": anime_title, "page": page}
        )

        AnimechanAPI._check_response_code(response.status_code)

        return [Quote(**quote) for quote in response.json()]

    def search_by_character_name(
        self, character_name: str, page: int = 1
    ) -> typing.List[Quote]:
        """
        Return a list of quotes from the given character.
        """
        response = requests.get(
            f"{self.endpoint}/quotes/character",
            params={"name": character_name, "page": page},
        )

        AnimechanAPI._check_response_code(response.status_code)

        return [Quote(**quote) for quote in response.json()]

    @staticmethod
    def _check_response_code(status_code: int, msg: str = ""):
        if status_code == 404:
            raise exceptions.NotFound()
        if status_code != 200:
            raise exceptions.ServerError(status_code=status_code, msg=msg)
