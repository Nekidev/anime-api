from dataclasses import dataclass

import typing

import pykakasi


@dataclass
class Image:
    """
    Object representation of an image
    """

    url: str


@dataclass
class Quote:
    """
    Object representation of a quote
    """

    id: int
    anime: str
    character: str
    quote: str


@dataclass
class _WaifuName:
    english: str
    japanese: str
    alternative: str

    @property
    def romaji(self):
        """
        Returns the romaji version of the name
        """
        return ' '.join(item['hepburn'] for item in pykakasi.kakasi().convert(self.japanese))


@dataclass
class _WaifuSource:
    name: str
    type_: str


@dataclass
class _WaifuStats:
    favorites: int
    love: int
    hate: int
    upvotes: int
    downvotes: int


@dataclass
class Waifu:
    """
    Object representation of a waifu
    """

    id: int
    name: _WaifuName
    images: typing.List[Image]
    from_: _WaifuSource
    statistics: _WaifuStats


@dataclass
class Fact:
    """
    Object representation of a fact
    """

    id: int
    fact: str
    tags: typing.List[str]
