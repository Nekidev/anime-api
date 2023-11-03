"""
Base module for the Neko-Love API. Documentation can be found at
https://docs.neko-love.xyz/

There will not be support for the v2 API, as it does not relate to anime or manga.
"""
import typing
import requests

from anime_api import exceptions
from anime_api.apis.neko_love.types import ImageCategory
from anime_api.apis.neko_love.objects import Image


class NekoLoveAPI:
    """
    Docs: https://docs.neko-love.xyz/
    """

    endpoint = "https://neko-love.xyz/api/v1"

    def get_random_image(
        self, category: typing.Union[ImageCategory.SFW, ImageCategory.NSFW]
    ) -> Image:
        """
        Returns a random image in the specific category
        """

        reponse = requests.get(self.endpoint + "/" + category.value)

        if reponse.status_code != 200:
            raise exceptions.ServerError(
                status_code=reponse.status_code, msg=reponse.json()["message"]
            )

        return Image(
            url=reponse.json()["url"],
            nsfw=isinstance(category, ImageCategory.NSFW),
        )
