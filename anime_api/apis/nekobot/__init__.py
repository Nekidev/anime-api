"""
Base module for the NekoBot API. Documentation can be found at
https://docs.nekobot.xyz
"""
from urllib.parse import quote_plus

import typing
import requests

from anime_api import exceptions
from anime_api.apis.nekobot.types import ImageGenType, ImageCategory
from anime_api.apis.nekobot.objects import Image


class NekoBotAPI:
    """
    Docs: https://docs.nekobot.xyz
    """

    endpoint = "https://nekobot.xyz/api"
    donator_api_key = None

    def __init__(self, donator_api_key: typing.Optional[str] = None):
        self.donator_api_key = donator_api_key

    def generate_image(self, image_type: ImageGenType, **kwargs):
        """
        Generates an image from the given image type
        """

        params = {"type": image_type.value}
        params.update(kwargs)

        response = requests.get(self.endpoint + "/imagegen", params=params)

        if (
            response.status_code != 200
            or response.json().get("success", False) is False
        ):
            raise exceptions.ServerError(
                status_code=response.status_code, msg=response.json()["message"]
            )

        return Image(
            url=response.json()["message"],
            color=response.json().get("color", None),
            nsfw=isinstance(image_type, ImageCategory.NSFW),
        )

    def get_random_image(
        self, category: typing.Union[ImageCategory.SFW, ImageCategory.NSFW, ImageCategory.BOTH]
    ) -> Image:
        """
        Returns a random image from the given category
        """

        if ImageCategory().is_donator_only(category) and not self.donator_api_key:
            raise exceptions.Forbidden(
                "This image category is only for donators. If you have a donator api key, initialize the class setting donator_api_key to your api key."
            )

        response = requests.get(
            self.endpoint + "/image", params={"type": category.value}
        )

        if (
            response.status_code != 200
            or response.json().get("success", False) is False
        ):
            raise exceptions.ServerError(
                status_code=response.status_code, msg=response.json()["message"]
            )

        return Image(
            url=response.json()["message"],
            color=response.json().get("color", None),
            nsfw=isinstance(category, ImageCategory.NSFW),
        )
