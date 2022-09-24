"""
Base module for the nekos.moe API. Documentation can be found at
https://docs.nekos.moe/
"""
import typing
import datetime
import json
import requests

from anime_api import exceptions
from anime_api.apis.nekos_moe.objects import User, Image, PendingImage
from anime_api.apis.nekos_moe.types import SearchSort


class NekosMoeAPI:
    """
    Docs: https://docs.nekos.moe/
    """

    endpoint = "https://nekos.moe/api/v1"
    api_token = None

    def __init__(
        self,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        api_token: typing.Optional[str] = None,
    ):
        if api_token:
            self.api_token = api_token
        elif username and password:
            self.api_token = self.get_api_token(username, password)

    def get_api_token(self, username: str, password: str) -> str:
        """
        Get an API token from username and password.
        """

        response = requests.post(
            f"{self.endpoint}/auth",
            json={"username": username, "password": password},
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        return response.json()["token"]

    def regenerate_api_token(
        self,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ) -> bool:
        """
        Regenerate the API token.
        """

        response = requests.post(
            f"{self.endpoint}/auth/regen",
            headers={"Authorization": self.api_token} if self.api_token else None,
        )

        if response.status_code != 204:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        if username and password:
            self.api_token = self.get_api_token(username, password)
        elif username or password:
            raise ValueError("You must provide both a username and password.")
        elif username or password:
            raise ValueError("You must provide a username and password. You provided only one.")

        return True

    def get_user(self, user_id: str = "@me") -> User:
        """
        Get information about a user.
        """

        response = requests.get(
            f"{self.endpoint}/user/{user_id}",
            headers={"Authorization": self.api_token} if self.api_token else None,
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        user = response.json()["user"]

        return User(
            _api=self,
            _id=user["id"],
            _username=user.get("username"),
            _created_at=datetime.datetime.fromisoformat(
                user["createdAt"].replace("Z", "+00:00")
            ),
            _verified=user.get("verified"),
            _favorites=[Image(_api=self, _id=id) for id in user.get("favorites", [])],
            _favorites_received=user.get("favoritesReceived"),
            _likes=[Image(_api=self, _id=id) for id in user.get("likes", [])],
            _likes_received=user.get("likesReceived"),
            _roles=user.get("roles"),
            _saved_tags=user.get("savedTags"),
            _uploads=user.get("uploads"),
        )

    def search_user(
        self, query: str, limit: int = 20, offset: int = 0
    ) -> typing.List[User]:
        """
        Search for a user.
        """

        response = requests.post(
            f"{self.endpoint}/users/search",
            headers={"Authorization": self.api_token} if self.api_token else None,
            data={"query": query, "limit": limit, "offset": offset},
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        return [
            User(
                _api=self,
                _id=user["id"],
                _username=user.get("username"),
                _created_at=datetime.datetime.fromisoformat(
                    user["createdAt"].replace("Z", "+00:00")
                )
                if user.get("createdAt")
                else None,
                _verified=user.get("verified"),
                _favorites=[
                    Image(_api=self, _id=id) for id in user.get("favorites", [])
                ],
                _favorites_received=user.get("favoritesReceived"),
                _likes=[Image(_api=self, _id=id) for id in user.get("likes", [])],
                _likes_received=user.get("likesReceived"),
                _roles=user.get("roles"),
                _saved_tags=user.get("savedTags"),
                _uploads=user.get("uploads"),
            )
            for user in response.json()["users"]
        ]

    def get_image(self, image_id: str) -> Image:
        """
        Get information about an image.
        """

        response = requests.get(
            f"{self.endpoint}/images/{image_id}",
            headers={"Authorization": self.api_token} if self.api_token else None,
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        image = response.json()["image"]

        return Image(
            _api=self,
            _id=image["id"],
            _created_at=datetime.datetime.fromisoformat(
                image["createdAt"].replace("Z", "+00:00")
            ),
            _tags=image["tags"],
            _uploader=User(
                _api=self,
                _id=image["uploader"]["id"],
                _username=image["uploader"]["username"],
            ),
            _approver=User(
                _api=self,
                _id=image["approver"]["id"],
                _username=image["approver"]["username"],
            )
            if "approver" in image
            else None,
            _favorites=image["favorites"],
            _likes=image["likes"],
        )

    def search_images(
        self,
        nsfw: typing.Optional[bool] = None,
        uploader_username: typing.Optional[str] = None,
        artist: typing.Optional[str] = None,
        tags: typing.Optional[typing.List[str]] = None,
        sort: typing.Optional[SearchSort] = None,
        posted_before: typing.Optional[datetime.datetime] = None,
        posted_after: typing.Optional[datetime.datetime] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> typing.List[Image]:
        """
        Search for images.
        """

        params = {}

        if nsfw is not None:
            params["nsfw"] = nsfw

        if uploader_username:
            params["uploader"] = uploader_username

        if artist:
            params["artist"] = artist

        if tags:
            params["tags"] = tags

        if sort:
            params["sort"] = sort.value

        if posted_before:
            params["posted_before"] = posted_before.timestamp() * 1000

        if posted_after:
            params["posted_after"] = posted_after.timestamp() * 1000

        if limit:
            if limit > 50 or limit < 1:
                raise ValueError("Limit must be between 1 and 50.")
            params["limit"] = limit

        if offset:
            if offset < 0 or offset > 2500:
                raise ValueError("Offset must be between 0 and 2500.")
            params["offset"] = offset

        response = requests.post(
            f"{self.endpoint}/images/search",
            data=json.dumps(params),
            headers={"Authorization": self.api_token} if self.api_token else None,
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        images = response.json()["images"]

        return [
            Image(
                _api=self,
                _id=image["id"],
                _nsfw=image["nsfw"],
                _tags=image["tags"],
                _likes=image["likes"],
                _favorites=image["favorites"],
                _uploader=User(
                    _api=self,
                    _id=image["uploader"]["id"],
                    _username=image["uploader"]["username"],
                ),
                _approver=User(
                    _api=self,
                    _id=image["approver"]["id"],
                    _username=image["approver"]["username"],
                )
                if "approver" in image
                else None,
                _created_at=datetime.datetime.fromisoformat(
                    image["createdAt"].replace("Z", "+00:00")
                ),
            )
            for image in images
        ]

    def get_random_images(self, count: int) -> typing.List[Image]:
        """
        Get random images.
        """

        response = requests.get(
            f"{self.endpoint}/random/image",
            headers={"Authorization": self.api_token} if self.api_token else None,
            params={"count": count},
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        return [
            Image(
                _api=self,
                _id=image.get("id"),
                _nsfw=image.get("nsfw"),
                _tags=image.get("tags"),
                _likes=image.get("likes"),
                _favorites=image.get("favorites"),
                _uploader=User(
                    _api=self,
                    _id=image["uploader"]["id"],
                    _username=image["uploader"]["username"],
                ),
                _approver=User(
                    _api=self,
                    _id=image["approver"]["id"],
                    _username=image["approver"]["username"],
                )
                if "approver" in image
                else None,
                _created_at=datetime.datetime.fromisoformat(
                    image["createdAt"].replace("Z", "+00:00")
                ),
            )
            for image in response.json()["images"]
        ]

    def upload_image(
        self,
        image: typing.Union[str, bytes],
        nsfw: bool,
        artist: str,
        tags: typing.List[str],
    ) -> PendingImage:
        """
        Upload an image.
        """

        if isinstance(image, str):
            with open(image, "rb") as file:
                image = file.read()

        response = requests.post(
            f"{self.endpoint}/images",
            files={"image": image},
            data={"nsfw": nsfw, "artist": artist, "tags": tags},
            headers={"Authorization": self.api_token} if self.api_token else None,
        )

        if response.status_code != 200:
            raise exceptions.ServerError(
                status_code=response.status_code,
                msg=response.json().get("message", "Unknown error"),
            )

        image_urls = response.json()

        return PendingImage(
            image=Image(
                _api=self,
                _id=image_urls["image"].get("id"),
                _nsfw=image_urls["image"].get("nsfw"),
                _tags=image_urls["image"].get("tags"),
                _likes=image_urls["image"].get("likes"),
                _favorites=image_urls["image"].get("favorites"),
                _uploader=User(
                    _api=self,
                    _id=image_urls["image"].get("uploader", {}).get("id", None),
                    _username=image_urls["image"]
                    .get("uploader", {})
                    .get("username", None),
                ),
                _approver=User(
                    _api=self,
                    _id=image_urls["image"].get("approver", {}).get("id", None),
                    _username=image_urls["image"]
                    .get("approver", {})
                    .get("username", None),
                )
                if "approver" in image_urls["image"]
                else None,
                _created_at=datetime.datetime.fromisoformat(
                    image_urls["image"].get("createdAt", None).replace("Z", "+00:00")
                )
                if image_urls["image"].get("createdAt", None)
                else None,
                _pending=True,
            ),
            image_url=image_urls["image_url"],
            post_url=image_urls["post_url"],
        )
