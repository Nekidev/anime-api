from dataclasses import dataclass
from datetime import datetime

import typing

from .types import ImageTag


@dataclass
class _ImageDimensions:
    height: int
    width: int


@dataclass
class Image:
    """
    Object representation of an image.
    """

    id: int
    signature: typing.Optional[str] = None
    extension: typing.Optional[str] = None
    favorites: typing.Optional[int] = None
    dominant_color: typing.Optional[str] = None
    source: typing.Optional[str] = None
    uploaded_at: typing.Optional[datetime] = None
    is_nsfw: typing.Optional[bool] = None
    dimens: typing.Optional[_ImageDimensions] = None
    url: typing.Optional[str] = None
    preview_url: typing.Optional[str] = None
    tags: typing.Optional[
        typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
    ] = None
