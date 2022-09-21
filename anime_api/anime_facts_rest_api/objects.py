from dataclasses import dataclass


@dataclass
class Anime:
    """
    Object representation of an anime
    """

    id: int
    name: str
    image: str


@dataclass
class Fact:
    """
    Object representation of an anime fact
    """

    id: int
    fact: str
