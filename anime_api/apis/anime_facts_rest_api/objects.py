from dataclasses import dataclass

import typing


@dataclass
class Anime:
    """
    Object representation of an anime
    """

    id: int
    name: str
    image: str

    @property
    def facts(self):
        """
        Returns a list of facts about the anime.
        """
        from anime_api.apis import AnimeFactsRestAPI

        api = AnimeFactsRestAPI()

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
