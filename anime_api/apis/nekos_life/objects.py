from dataclasses import dataclass


@dataclass
class Image:
    """
    Object representation of an image
    """

    url: str


@dataclass
class EightBall:
    """
    Object representation of an 8ball response
    """

    answer: str
    image: Image


@dataclass
class Fact:
    """
    Object representation of a fact
    """

    fact: str
