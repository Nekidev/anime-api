from dataclasses import dataclass

import typing


@dataclass
class _AnimeTitle:
    """
    Object representation of an anime's titles
    """

    romaji: str
    synonyms: typing.List[str]
    native: typing.Optional[str] = None
    english: typing.Optional[str] = None


@dataclass
class Anime:
    """
    Object representation of an anime.
    """
    anilist_id: int
    mal_id: typing.Optional[int]
    title: typing.Optional[_AnimeTitle]
    is_adult: typing.Optional[bool]


@dataclass
class Result:
    """
    Object representation of a result of a search.
    """
    anime: Anime
    filename: str
    episode: typing.Optional[int]
    from_: typing.Optional[float]
    to: typing.Optional[float]
    similarity: float
    video: typing.Optional[str]
    image: typing.Optional[str]
