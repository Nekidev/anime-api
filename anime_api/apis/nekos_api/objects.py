from dataclasses import dataclass
from datetime import datetime

import typing

from dateutil import parser

from anime_api.apis.nekos_api.types import NsfwLevel, ImageOrientation
from anime_api.utils import to_snake


@dataclass
class Artist:
    """
    Object representation of an artist
    """

    id: str
    name: str
    url: typing.Optional[str]
    images: typing.Optional[int] = None


@dataclass
class _Source:
    name: str
    url: str


@dataclass
class Category:
    """
    Object representation of a category
    """

    id: str
    name: str
    description: str
    nsfw: bool
    type: str
    created_at: datetime
    images: typing.Optional[int] = None


@dataclass
class Character:
    """
    Object representation of a character
    """

    id: str
    name: str
    description: str
    source: str
    created_at: datetime
    images: typing.Optional[int] = None


@dataclass
class _Dimens:
    height: int
    width: int
    aspect_ratio: str
    orientation: ImageOrientation

@dataclass
class Image:
    """
    Object representation of an image
    """

    id: str
    url: str
    artist: typing.Optional[Artist]
    source: typing.Optional[_Source]
    original: typing.Optional[bool]
    nsfw: NsfwLevel
    categories: typing.List[Category]
    characters: typing.List[Character]
    created_at: datetime
    etag: str
    size: int
    mimetype: str
    color: str
    expires: datetime
    dimens: _Dimens

    def from_json(data: dict) -> 'Image':
        return Image(
            id=data["id"],
            url=data["url"],
            artist=Artist(**data["artist"]) if data["artist"] else None,
            source=_Source(**data["source"]) if data["source"] else None,
            original=data["original"],
            nsfw=NsfwLevel(data["nsfw"]),
            categories=[Category(**to_snake(c)) for c in data["categories"]],
            characters=[Character(**to_snake(c)) for c in data["characters"]],
            created_at=parser.parse(data["createdAt"]),
            etag=data["meta"]["eTag"],
            size=data["meta"]["size"],
            mimetype=data["meta"]["mimetype"],
            color=data["meta"]["color"],
            expires=parser.parse(data["meta"]["expires"]),
            dimens=_Dimens(
                height=data["meta"]["dimens"]["height"],
                width=data["meta"]["dimens"]["width"],
                aspect_ratio=data["meta"]["dimens"]["height"],
                orientation=ImageOrientation(data["meta"]["dimens"]["orientation"]),
            ),
        )
