from dataclasses import dataclass

import typing


@dataclass
class Anime:
    """
    Object representation of an anime
    """
    _api: object

    id: int
    name: str
    image: str

    def facts(self, api: typing.Optional[object] = None):
        """
        Returns a list of facts about the anime.
        """
        if not api and not self._api:
            raise ValueError(
                "No API was provided."
            )
        elif not api:
            api = self._api

        return api.get_anime_facts(self.name)

    def __str__(self):
        return self.name.replace('_', ' ').title()


@dataclass
class Fact:
    """
    Object representation of an anime fact
    """

    id: int
    fact: str

    def __str__(self):
        return self.fact
