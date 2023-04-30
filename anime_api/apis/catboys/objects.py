from dataclasses import dataclass


@dataclass
class _Artist:
    name: str
    url: str


@dataclass
class Image:
    url: str
    artist: _Artist
    source_url: str

    def from_json(data: dict):
        return Image(
            url=data["url"],
            artist=_Artist(data["artist"], data["artist_url"]),
            source_url=data["source_url"],
        )


@dataclass
class EightBall:
    answer: str
    image: str

    def from_json(data: dict):
        return EightBall(answer=data["response"], image=data["url"])


@dataclass
class DiceRoll:
    number: int
    image: str

    def from_json(data: dict):
        return DiceRoll(number=data["response"], image=data["url"])
