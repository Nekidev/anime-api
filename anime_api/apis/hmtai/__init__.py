"""
Base module for the Hmtai API. Endpoints can be found at https://hmtai.herokuapp.com/v2/endpoints
"""
import typing
import requests

from anime_api import exceptions
from anime_api.apis.hmtai.types import ImageCategory
from anime_api.apis.hmtai.objects import Image


class HmtaiAPI:
    """
    Endpoints: https://hmtai.hatsunia.cfd/v2/endpoints
    """

    endpoint = "https://hmtai.hatsunia.cfd/v2"

    def get_random_image(
        self, category: typing.Union[ImageCategory.SFW, ImageCategory.NSFW]
    ) -> Image:
        """
        Returns a random image with in the specified category.
        """

        response = requests.get(self.endpoint + "/" + category.value)

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return Image(
            url=response.json()["url"], nsfw=isinstance(category, ImageCategory.NSFW)
        )
