"""
Base module for the Nekos.Life API. Documentation can be found at
https://api.nekos.dev/api/v2/endpoints
"""
import requests

from anime_api import exceptions
from anime_api.apis.nekos_life.objects import Image, EightBall, Fact
from anime_api.apis.nekos_life.types import ImageType


class NekosLifeAPI:
    """
    Docs
    """

    endpoint = "https://nekos.life/api/v2"

    def get_eight_ball(self) -> EightBall:
        """
        Returns a random 8ball prediction.
        """

        response = requests.get(f"{self.endpoint}/8ball")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        data = response.json()

        return EightBall(
            answer=data["response"],
            image=Image(
                url=data["url"]
            )
        )

    def get_random_cat_emoji(self) -> str:
        """
        Returns a random cat text emoji
        """

        response = requests.get(f"{self.endpoint}/cat")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return response.json()["cat"]

    def get_random_fact(self) -> Fact:
        """
        Returns a random fact
        """

        response = requests.get(f"{self.endpoint}/fact")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        data = response.json()

        return Fact(
            fact=data["fact"],
        )

    def get_random_name(self) -> str:
        """
        Returns a random name
        """

        response = requests.get(f"{self.endpoint}/name")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return response.json()["name"]

    def get_random_image(self, category: ImageType) -> Image:
        """
        Returns a random image
        """

        response = requests.get(f"{self.endpoint}/img/{category.value}")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return Image(
            url=response.json()["url"]
        )

    def owoify(self, text: str) -> str:
        """
        OwOifies a string
        """

        if len(text) > 200:
            raise ValueError("Text must be less than 200 characters")

        response = requests.get(f"{self.endpoint}/owoify", params={"text": text})

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return response.json()["owo"]

    def spoiler(self, text: str) -> str:
        """
        Spoilerifies a string
        """

        if len(text) > 200:
            raise ValueError("Text must be less than 200 characters")

        response = requests.get(f"{self.endpoint}/spoiler", params={"text": text})

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return response.json()["owo"]

    def get_random_why(self) -> str:
        """
        Returns a random why question
        """

        response = requests.get(f"{self.endpoint}/why")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        return response.json()["why"]
