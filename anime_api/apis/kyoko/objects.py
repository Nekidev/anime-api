from dataclasses import dataclass


@dataclass
class Quote:
    """
    Object representing a quote. Anime and character are not objects because the API returns a
    title (for the anime) or a name (for the character).
    """

    id: int
    anime: str
    character: str
    quote: str


@dataclass
class Image:
    """
    Object representing an image.
    """

    url: str
