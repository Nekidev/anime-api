"""
Base module for the Catboys API. Endpoints can be found at https://catboys.com/api
"""
import typing
import requests

from anime_api import exceptions

from anime_api.apis.catboys.objects import Image, EightBall, DiceRoll


class CatboysAPI:
    """
    Endpoints: https://api.catboys.com/endpoints
    """

    endpoint: str = "https://api.catboys.com"

    def __init__(self, endpoint: typing.Optional[str] = None):
        self.endpoint = endpoint or self.endpoint

    def get_random_image(self) -> Image:
        """
        Returns a random image.
        """

        response = requests.get(self.endpoint + "/img")
        CatboysAPI._check_response_code(response)

        return Image.from_json(response.json())

    def get_random_baka_gif(self) -> str:
        """
        Returns a random baka gif.
        """

        response = requests.get(self.endpoint + "/baka")
        CatboysAPI._check_response_code(response)

        return response.json()["url"]

    def get_eight_ball(self) -> EightBall:
        """
        Returns an 8ball prediction.
        """

        response = requests.get(self.endpoint + "/8ball")
        CatboysAPI._check_response_code(response)

        return EightBall.from_json(response.json())

    def get_dice_roll(self) -> DiceRoll:
        """
        Returns a random number and image from a virtual 6-sided dice.
        """

        response = requests.get(self.endpoint + "/dice")
        CatboysAPI._check_response_code(response)

        return DiceRoll.from_json(response.json())

    def get_catboy_saying(self) -> str:
        """
        Returns a random saying from a virtual catboy.
        """

        response = requests.get(self.endpoint + "/catboy")
        CatboysAPI._check_response_code(response)

        return response.json()["response"]

    @staticmethod
    def _check_response_code(res) -> None:
        """
        Check if the request was successful.
        """
        data = res.json()
        if (
            res.status_code not in range(200, 300)
            or data.get("error", "none") != "none"
        ):
            raise exceptions.ServerError(
                res.status_code,
                f"An error occurred while fetching the data from the server{'. ' + data['error'] if data.get('error', 'none') != 'none' else ''}",
            )
