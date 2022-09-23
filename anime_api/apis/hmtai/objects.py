from dataclasses import dataclass


@dataclass
class Image:
    """
    Object representation of an image
    """

    url: str
    nsfw: bool
