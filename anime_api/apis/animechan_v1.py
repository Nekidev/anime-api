"""Current Animechan quote API: https://animechan.io/docs.

The legacy AnimechanAPI class uses a retired service contract. This client
adapts the current nested response to the existing Quote dataclass.
"""
import typing

import requests

from anime_api import exceptions
from anime_api.apis.animechan.objects import Quote


class AnimechanV1API:
    """Random quotes, optionally filtered by anime or character.

    Free requests need no API key. See the provider docs for current limits.
    HTTP and transport errors propagate; requests are not automatically retried.
    """

    endpoint = "https://api.animechan.io/v1"

    def __init__(self, endpoint: typing.Optional[str] = None, timeout: float = 10):
        self.endpoint = (endpoint or self.endpoint).rstrip("/")
        self.timeout = timeout

    def get_random_quote(
        self,
        anime_title: typing.Optional[str] = None,
        character_name: typing.Optional[str] = None,
    ) -> Quote:
        """Fetch one quote. Supply at most one filter."""
        if anime_title and character_name:
            raise ValueError("Supply either anime_title or character_name, not both")
        params = {}
        if anime_title:
            params["anime"] = anime_title
        if character_name:
            params["character"] = character_name
        response = requests.get(
            self.endpoint + "/quotes/random", params=params, timeout=self.timeout
        )
        if response.status_code == 404:
            raise exceptions.NotFound()
        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)
        data = response.json()["data"]
        return Quote(
            anime=data["anime"]["name"],
            character=data["character"]["name"],
            quote=data["content"],
        )
