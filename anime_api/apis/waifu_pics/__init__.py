"""
Base module for the waifu.pics API. The API documentation can be found at
https://waifu.pics/docs
"""
import typing
import requests

from anime_api import exceptions
from anime_api.apis.waifu_pics.types import ImageCategory
from anime_api.apis.waifu_pics.objects import Image


class WaifuPicsAPI:
    """
    Docs: https://waifu.pics/docs
    """

    endpoint = "https://api.waifu.pics"

    def __init__(self, endpoint: typing.Optional[str] = None):
        self.endpoint = endpoint or self.endpoint

    def get_image(
        self, category: typing.Union[ImageCategory.SFW, ImageCategory.NSFW]
    ) -> Image:
        """
        Returns a random image from the API
        """

        response = requests.get(
            self.endpoint
            + f"/{'sfw' if isinstance(category, ImageCategory.SFW) else 'nsfw'}/{category.value}"
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code, msg=response.json()["message"]
            )

        return Image(
            url=response.json()["url"], nsfw=isinstance(category, ImageCategory.NSFW)
        )

    def get_many_images(
        self,
        category: typing.Union[ImageCategory.SFW, ImageCategory.NSFW],
        exclude: typing.Optional[typing.List[typing.Union[str, Image]]] = None,
    ) -> typing.List[Image]:
        """
        Returns a list of 30 images from a specific category
        """

        response = requests.post(
            self.endpoint
            + f"/many/{'sfw' if isinstance(category, ImageCategory.SFW) else 'nsfw'}/{category.value}",
            json={
                "exclude": [image.url if isinstance(image, Image) else image for image in exclude]
                if isinstance(exclude[0], Image)
                else exclude
            }
            if exclude and len(exclude) > 0
            else {},
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code, msg=response.json()["message"]
            )

        return [
            Image(url=image, nsfw=isinstance(category, ImageCategory.NSFW))
            for image in response.json()["files"]
        ]
