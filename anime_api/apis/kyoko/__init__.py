"""
Base module for the kyoko API. Documentation can be found at
https://github.com/Elliottophellia/kyoko
"""
import requests

from anime_api import exceptions
from anime_api.apis.kyoko.objects import Quote, Image


class KyokoAPI:
    """
    Docs: https://github.com/Elliottophellia/kyoko
    """

    endpoint = "https://api.rei.my.id/v3"

    def get_random_quote(self) -> Quote:
        """
        Get a random quote from the API.
        """
        response = requests.get(self.endpoint + "/quotes")
        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)
        return Quote(
            id=response.json()["id"],
            anime=response.json()["anime"],
            character=response.json()["name"],
            quote=response.json()["quote"],
        )

    def get_random_slap(self) -> Image:
        """
        Get a random slap image from the API.
        """
        response = requests.get(self.endpoint + "/slap")
        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)
        return Image(url=response.json()["url"])

    def get_random_kiss(self) -> Image:
        """
        Get a random kiss image from the API.
        """
        response = requests.get(self.endpoint + "/kiss")
        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)
        return Image(url=response.json()["url"])

    def get_random_hug(self) -> Image:
        """
        Get a random hug image from the API.
        """
        response = requests.get(self.endpoint + "/hug")
        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)
        return Image(url=response.json()["url"])
