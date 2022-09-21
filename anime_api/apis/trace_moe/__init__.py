"""
Base module for the trace.moe API. The API documentation can be found at
https://soruly.github.io/trace.moe-api/
"""
from dataclasses import dataclass

import typing
import requests

from anime_api import exceptions
from anime_api.apis.trace_moe.objects import Result, Anime, _AnimeTitle


@dataclass
class File:
    """
    Class representation of a file upload
    """

    file: typing.Optional[typing.Union[typing.BinaryIO, str]] = None
    content_type: typing.Optional[str] = None
    url: typing.Optional[str] = None

    def get_file_type(self):
        """
        Returns if the file is a binary file or a url
        """
        if self.file:
            return "file"
        elif self.url:
            return "url"
        else:
            return None


class TraceMoeAPI:
    """
    Docs: https://soruly.github.io/trace.moe-api/#/docs
    """

    endpoint = "https://api.trace.moe"
    x_trace_key: typing.Optional[str] = None

    _supported_file_types = [
        r"^image",
        r"^video",
    ]

    # If the limit is exceeded, the server will return a 413 error so the upload size is
    # checked before uploading.
    upload_limit = 1024 * 1024 * 25

    def __init__(
        self,
        endpoint: typing.Optional[str] = None,
        x_trace_key: typing.Optional[str] = None,
    ):
        if endpoint:
            self.endpoint = endpoint
        self.x_trace_key = x_trace_key

    def search(
        self, file: File, get_anime_info: bool = True, cut_black_borders: bool = False
    ) -> typing.List[dict]:
        """
        Search for an anime by it's image.
        """
        params = {}
        headers = {
            "X-Trace-Key": self.x_trace_key
        } if self.x_trace_key else None

        if get_anime_info:
            params["anilistInfo"] = ""
        if cut_black_borders:
            params["cutBorders"] = ""

        if file.get_file_type() == "file":
            if file.file.size > self.upload_limit:
                raise exceptions.UploadLimitExceeded(
                    "The file size exceeds the upload limit."
                )
            elif not any(
                file.content_type.startswith(i) for i in self._supported_file_types
            ):
                raise exceptions.UnsupportedFileType(
                    "The file type is not supported by the API."
                )

            response = requests.post(
                self.endpoint + "/search",
                params=params,
                headers=headers,
                files={"file": file.file},
            )

        elif file.get_file_type() == "url":
            params.update({"url": file.url})
            response = requests.post(
                self.endpoint + "/search",
                headers=headers,
                params=params,
            )

        if response.status_code == 413:
            raise exceptions.UploadLimitExceeded(
                "The file size exceeds the upload limit."
            )
        elif response.status_code != 200 or response.json()["error"] != "":
            raise exceptions.ServerError(status_code=response.status_code)

        return [
            Result(
                anime=Anime(
                    anilist_id=data["anilist"]["id"],
                    mal_id=data["anilist"]["idMal"],
                    title=_AnimeTitle(
                        romaji=data["anilist"]["title"]["romaji"],
                        native=data["anilist"]["title"]["native"],
                        english=data["anilist"]["title"]["english"],
                        synonyms=data["anilist"]["synonyms"],
                    ),
                    is_adult=data["anilist"]["isAdult"],
                )
                if isinstance(data["anilist"], dict)
                else Anime(
                    anilist_id=data["anilist"],
                    mal_id=None,
                    title=None,
                    is_adult=None,
                ),
                filename=data["filename"],
                episode=data["episode"],
                from_=data["from"],
                to=data["to"],
                similarity=data["similarity"],
                video=data["video"],
                image=data["image"],
            )
            for data in response.json()["result"]
        ]
