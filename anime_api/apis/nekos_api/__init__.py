# pylint: disable=expression-not-assigned, missing-timeout
"""
Base module for Nekos API. Documentation can be found at
https://nekos.nekidev.com/docs/rest-api/endpoints
"""
from urllib.parse import quote
from datetime import datetime
from functools import wraps

import typing
import time
import re

import requests

from anime_api import exceptions
from anime_api.apis.nekos_api.objects import Image, Artist, Character, Category
from anime_api.utils import to_snake


last_request: typing.Optional[datetime] = None


def prevent_ratelimit(func):
    """
    Sleeps necessary time before running a class method to prevent ratelimiting.
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        global last_request
        now = datetime.now()
        if last_request is None:
            # No request has been made.
            result = func(*args, **kwargs)
            last_request = datetime.now()
            return result

        elapsed_time = now - last_request
        wait_time = 1 - (elapsed_time.microseconds / 1000000)

        time.sleep(wait_time)

        result = func(*args, **kwargs)
        last_request = datetime.now()
        return result

    return decorator


class NekosAPI:
    """
    Docs: https://nekos.nekidev.com/docs/rest-api/endpoints
    """

    endpoint: str = "https://nekos.nekidev.com/api"
    token: typing.Optional[str] = None

    def __init__(
        self, endpoint: typing.Optional[str] = None, token: typing.Optional[str] = None
    ):
        self.endpoint = endpoint or self.endpoint

        if token:
            NekosAPI._validate_token(token)

        self.token = token

    @prevent_ratelimit
    def get_images(self, limit: int = 10, offset: int = 0):
        """
        Returns a list of images.
        * Requires a valid access token.
        """
        if not self.token:
            raise ValueError("You need a valid access token to use this method.")

        headers = {"Authorization": "Bearer " + self.token}
        params = {"limit": limit, "offset": offset}

        response = requests.get(
            self.endpoint + "/image", headers=headers, params=params
        )

        NekosAPI._check_response_code(response)

        data = response.json()

        return [Image.from_json(image) for image in data["data"]]

    @prevent_ratelimit
    def get_random_image(
        self, categories: typing.Optional[typing.List[str]] = None
    ) -> Image:
        """
        Returns a random image with the specified categories or completely
        random if categories are not specified.
        """
        params = {"categories": ",".join(categories)} if categories else {}

        response = requests.get(self.endpoint + "/image/random", params=params)

        NekosAPI._check_response_code(response)

        data = response.json()

        return Image.from_json(data["data"][0])

    @prevent_ratelimit
    def get_random_images(
        self, count: int = 10, categories: typing.Optional[typing.List[str]] = None
    ) -> typing.List[Image]:
        """
        Returns a certain amount of random images with the specified categories or completely
        random if categories are not specified.
        """
        params = {"limit": count}
        params.update({"categories": ",".join(categories)}) if categories else None

        response = requests.get(self.endpoint + "/image/random", params=params)

        NekosAPI._check_response_code(response)

        data = response.json()

        return [Image.from_json(image) for image in data["data"]]

    @prevent_ratelimit
    def get_image_by_id(self, image_id: str) -> Image:
        """
        Returns an image by its ID
        """
        response = requests.get(self.endpoint + "/image/" + quote(image_id))

        NekosAPI._check_response_code(response)

        data = response.json()

        return Image.from_json(data["data"])

    @prevent_ratelimit
    def get_artist_by_id(self, artist_id: str) -> Artist:
        """
        Returns an artist by its ID
        """
        response = requests.get(self.endpoint + "/artist/" + quote(artist_id))

        NekosAPI._check_response_code(response)

        data = response.json()

        return Artist(**to_snake(data["data"]))

    @prevent_ratelimit
    def get_images_by_artist_id(
        self, artist_id: str, limit: int = 10, offset: int = 0
    ) -> typing.List[Image]:
        """
        Returns all artist's images.
        """
        response = requests.get(
            self.endpoint + "/artist/" + quote(artist_id) + "/images",
            params={"limit": limit, "offset": offset},
        )

        NekosAPI._check_response_code(response)

        data = response.json()

        return [Image.from_json(image) for image in data["data"]]

    @prevent_ratelimit
    def get_categories(self, limit: int = 10, offset: int = 0) -> typing.List[Category]:
        """
        Returns a list of all categories.
        """
        response = requests.get(
            self.endpoint + "/category", params={"limit": limit, "offset": offset}
        )

        NekosAPI._check_response_code(response)

        data = response.json()

        return [Category(**to_snake(category)) for category in data["data"]]

    @prevent_ratelimit
    def get_category_by_id(self, category_id: str) -> Category:
        """
        Returns a category by it's ID.
        """
        response = requests.get(self.endpoint + "/category/" + quote(category_id))

        NekosAPI._check_response_code(response)

        data = response.json()

        return Category(**to_snake(data["data"]))

    @prevent_ratelimit
    def get_character_by_id(self, character_id: str) -> Character:
        """
        Returns a character by it's ID.
        """
        response = requests.get(self.endpoint + "/character/" + quote(character_id))

        NekosAPI._check_response_code(response)

        data = response.json()

        return Character(**to_snake(data["data"]))

    @staticmethod
    def _check_response_code(res) -> None:
        """
        Check if the request was successful.
        """
        data = res.json()
        success = data["success"]
        if res.status_code not in range(200, 300) or not success:
            raise exceptions.ServerError(
                res.status_code,
                f"An error occurred while fetching the data from the server{'. ' + data['message'] if 'message' in data else ''}",
            )

    @staticmethod
    def _validate_token(token) -> None:
        """
        Validate the API token.
        """
        exp = r"^[0-9a-zA-Z]{100}$"
        if len(re.findall(exp, token)) == 0:
            raise ValueError(
                "The token is invalid. It should be 100 characters long and contain numbers and lowercase/uppercase characters."
            )
