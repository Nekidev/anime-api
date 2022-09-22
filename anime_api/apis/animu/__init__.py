"""
Base module for the animu API. Documentation for the api can be found at
https://docs.animu.ml
"""
import typing
import requests

from anime_api import exceptions
from anime_api.apis.animu.objects import (
    Image,
    Quote,
    Waifu,
    _WaifuName,
    _WaifuSource,
    _WaifuStats,
    Fact,
)
from anime_api.apis.animu.types import ImageType
from anime_api.apis.animu.operators import AND, OR


class AnimuAPI:
    """
    Docs: https://docs.animu.ml
    """

    endpoint = "https://api.animu.ml"
    api_token: str

    def __init__(self, api_token: str):
        self.api_token = api_token

    def get_random_image(self, category: ImageType) -> Image:
        """
        Returns a random image for the specific category.
        """

        response = requests.get(
            self.endpoint + "/" + category.value, headers={"Auth": self.api_token}
        )

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return Image(url=response.json()["url"])

    def get_random_quote(self) -> Quote:
        """
        Returns a random quote
        """

        response = requests.get(
            self.endpoint + "/quote", headers={"Auth": self.api_token}
        )

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return Quote(
            id=response.json()["_id"],
            anime=response.json()["anime"],
            quote=response.json()["quote"],
            character=response.json()["said"],
        )

    def get_random_waifu(self) -> Waifu:
        """
        Returns a random waifu
        """

        response = requests.get(
            self.endpoint + "/waifu", headers={"Auth": self.api_token}
        )

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return Waifu(
            id=response.json()["_id"],
            name=_WaifuName(
                english=response.json()["name"]["en"],
                japanese=response.json()["name"]["jp"],
                alternative=response.json()["name"]["alt"],
            ),
            images=[Image(url=image) for image in response.json()["images"]],
            from_=_WaifuSource(
                name=response.json()["from"]["name"],
                type_=response.json()["from"]["type"],
            ),
            statistics=_WaifuStats(
                favorites=response.json()["stats"]["favs"],
                love=response.json()["stats"]["love"],
                hate=response.json()["stats"]["hate"],
                upvotes=response.json()["stats"]["upvote"],
                downvotes=response.json()["stats"]["downvote"],
            ),
        )

    def get_random_fact(
        self, 
        tags: typing.Optional[typing.Union[str, typing.List[typing.Union[AND, OR]]]] = None,
        min_length: typing.Optional[int] = None,
        max_length: typing.Optional[int] = None,
    ) -> Fact:
        """
        Returns a list of facts
        """

        tags = str(tags) if tags else ""

        response = requests.get(
            self.endpoint + "/fact",
            params={"tags": tags},
            headers={"Auth": self.api_token},
        )

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return Fact(
            id=response.json()["_id"],
            fact=response.json()["fact"],
            tags=response.json()["tags"],
        )
