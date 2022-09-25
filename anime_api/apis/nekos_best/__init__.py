"""
Base module for the nekos.best API. Documentation can be found at https://docs.nekos.best
"""
import typing
import requests

from anime_api import exceptions
from anime_api.apis.nekos_best.objects import Image, Artist, Anime
from anime_api.apis.nekos_best.types import ImageCategory, ImageType


class NekosBest:
    """
    Docs: https://docs.nekos.best/
    """

    endpoint = "https://nekos.best/api/v2"

    def get_random_images(
        self, image_type: ImageCategory, amount: int = 1
    ) -> typing.List[Image]:
        """
        Returns a list of random images
        """

        if amount < 1 or amount > 20:
            raise ValueError("Amount must be between 1 and 20")

        response = requests.get(
            self.endpoint + "/" + image_type.value, params={"amount": amount}
        )

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return [
            Image(
                url=image["url"],
                artist=Artist(
                    url=image["artist_href"],
                    name=image["artist_name"],
                )
                if "artist_href" in image
                else None,
                anime=Anime(
                    title=image["anime_name"],
                )
                if "anime_name" in image
                else None,
                source_url=image["source_url"] if "source_url" in image else None,
            )
            for image in response.json()["results"]
        ]

    def search_images(
        self,
        query: str,
        image_category: typing.Optional[ImageCategory] = None,
        image_type: typing.Optional[ImageType] = None,
        amount: int = 1,
    ) -> typing.List[Image]:
        """
        Returns a list of images that match the query
        """

        if amount < 1 or amount > 25:
            raise ValueError("Amount must be between 1 and 25")

        params = {
            "query": query,
            "amount": amount,
        }

        if image_type:
            params["type"] = image_type.value

        if image_category:
            params["category"] = image_category.value

        response = requests.get(self.endpoint + "/search", params=params)

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return [
            Image(
                url=image["url"],
                artist=Artist(
                    url=image["artist_href"],
                    name=image["artist_name"],
                )
                if "artist_href" in image
                else None,
                anime=Anime(
                    title=image["anime_name"],
                )
                if "anime_name" in image
                else None,
                source_url=image["source_url"] if "source_url" in image else None,
            )
            for image in response.json()["results"]
        ]
