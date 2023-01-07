"""
Base module for the waifu.im API. The API documentation can be found at
https://waifu.im/docs/
"""
import typing
import requests

from anime_api import exceptions

from .types import ImageTag, SearchSort, ImageOrientation
from .objects import Image, _ImageDimensions


class WaifuImAPI:
    """
    Docs: https://waifu.im/docs/
    """

    endpoint = "https://api.waifu.im"

    def __init__(self, endpoint: typing.Optional[str] = None):
        self.endpoint = endpoint or self.endpoint

    def __get_random_images(
        self,
        many: bool = False,
        tags: typing.Optional[
            typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
        ] = None,
        excluded_tags: typing.Optional[
            typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
        ] = None,
        included_files: typing.Optional[typing.List[str]] = None,
        excluded_files: typing.Optional[typing.List[str]] = None,
        is_nsfw: typing.Optional[bool] = None,
        is_gif: bool = False,
        order_by: typing.Optional[SearchSort] = SearchSort.RANDOM,
        orientation: typing.Optional[ImageOrientation] = None,
    ) -> typing.List[Image]:
        params = {
            "included_tags": ",".join([tag.value for tag in tags]) if tags else None,
            "excluded_tags": ",".join([tag.value for tag in excluded_tags])
            if excluded_tags
            else None,
            "is_nsfw": is_nsfw,
            "gif": is_gif,
            "order_by": order_by.value,
            "orientation": orientation.value if orientation else None,
            "included_files": ",".join(included_files) if included_files else None,
            "excluded_files": ",".join(excluded_files) if excluded_files else None,
            "many": many,
        }
        headers = {}

        response = requests.get(
            f"{self.endpoint}/search/", params=params, headers=headers
        )
        if response.status_code != 200:
            raise exceptions.ServerError(
                response.status_code, msg=response.json().get("detail")
            )

        return [
            Image(
                id=image["image_id"],
                signature=image["signature"],
                extension=image["extension"],
                favorites=image["favourites"],
                dominant_color=image["dominant_color"],
                source=image["source"],
                uploaded_at=image["uploaded_at"],
                is_nsfw=image["is_nsfw"],
                dimens=_ImageDimensions(
                    width=image["width"],
                    height=image["height"],
                ),
                url=image["url"],
                preview_url=image["preview_url"],
                tags=[ImageTag().get_tag(tag["name"]) for tag in image["tags"]],
            )
            for image in response.json()["images"]
        ]

    def get_random_image(
        self,
        tags: typing.Optional[
            typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
        ] = None,
        excluded_tags: typing.Optional[
            typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
        ] = None,
        selected_file: typing.Optional[typing.List[str]] = None,
        excluded_files: typing.Optional[typing.List[str]] = None,
        is_nsfw: typing.Optional[bool] = None,
        is_gif: bool = False,
        order_by: typing.Optional[SearchSort] = SearchSort.RANDOM,
        orientation: typing.Optional[ImageOrientation] = None,
    ) -> Image:
        """
        Get a random image.
        """

        return self.__get_random_images(
            many=False,
            tags=tags,
            excluded_tags=excluded_tags,
            included_files=selected_file,
            excluded_files=excluded_files,
            is_nsfw=is_nsfw,
            is_gif=is_gif,
            order_by=order_by,
            orientation=orientation,
        )[0]

    def get_many_random_images(
        self,
        tags: typing.Optional[
            typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
        ] = None,
        excluded_tags: typing.Optional[
            typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
        ] = None,
        included_files: typing.Optional[typing.List[str]] = None,
        excluded_files: typing.Optional[typing.List[str]] = None,
        is_nsfw: typing.Optional[bool] = None,
        is_gif: bool = False,
        order_by: typing.Optional[SearchSort] = SearchSort.RANDOM,
        orientation: typing.Optional[ImageOrientation] = None,
    ) -> typing.List[Image]:
        """
        Get many random images.
        """

        return self.__get_random_images(
            many=True,
            tags=tags,
            excluded_tags=excluded_tags,
            included_files=included_files,
            excluded_files=excluded_files,
            is_nsfw=is_nsfw,
            is_gif=is_gif,
            order_by=order_by,
            orientation=orientation,
        )
