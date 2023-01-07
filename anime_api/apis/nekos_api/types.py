import typing

from enum import Enum


class NsfwLevel(Enum):
    UNKNOWN = None
    SFW = "sfw"
    QUESTIONABLE = "questionable"
    NSFW = "nsfw"


class ImageOrientation(Enum):
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"
    SQUARE = "square"
