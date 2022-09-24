from dataclasses import dataclass

import typing


@dataclass
class Artist:
    """
    Object representation of an image's artist
    """

    url: typing.Optional[str] = None
    name: typing.Optional[str] = None


@dataclass
class Anime:
    """
    Object representation of an anime
    """

    title: str


@dataclass
class Image:
    """
    Object representation of an image
    """

    url: str
    artist: typing.Optional[Artist] = None
    anime: typing.Optional[Anime] = None
    source_url: typing.Optional[str] = None
