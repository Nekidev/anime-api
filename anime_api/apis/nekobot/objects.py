from dataclasses import dataclass

import typing


@dataclass
class Image:
    """
    Object representation of an image
    """

    url: str
    color: typing.Optional[int] = None
    nsfw: bool = True
