"""
Base module for Studio Ghibli API. Documentation can be found at
https://ghibliapi.herokuapp.com/
"""
import typing
import requests

from anime_api import exceptions
from anime_api.apis.studio_ghibli_api.objects import Anime, _AnimeTitle, Person, Location, Species, Vehicle


class StudioGhibliAPI:
    """
    Base class for the Studio Ghibli API
    """

    endpoint = "https://ghibliapi.dev"

    def __init__(self, endpoint: typing.Optional[str] = None) -> None:
        self.endpoint = endpoint or self.endpoint

    def get_animes(self, limit: int = 50) -> typing.List[Anime]:
        """
        Get all animes. This is limited to 50 by default (Also 50 in the API if the param is not
        provided).
        """

        response = requests.get(f"{self.endpoint}/films", params={"limit": limit})

        if response.status_code != 200:
            raise exceptions.ServerError(response)

        return [
            Anime(
                _url=anime["url"],
                _title=_AnimeTitle(
                    english=anime["title"],
                    japanese=anime["original_title"],
                    romaji=anime["original_title_romanised"],
                ),
                _description=anime["description"],
                _director=anime["director"],
                _producer=anime["producer"],
                _release_date=int(anime["release_date"]),
                _running_time=int(anime["running_time"]),
                _rt_score=int(anime["rt_score"]),
                _people=anime["people"],
                _species=anime["species"],
                _locations=anime["locations"],
                _vehicles=anime["vehicles"],
            )
            for anime in response.json()
        ]

    def get_anime(self, anime_id: str) -> Anime:
        """
        Get an anime by ID
        """

        response = requests.get(f"{self.endpoint}/films/{anime_id}")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        anime = response.json()

        return Anime(
            _url=anime["url"],
            _title=_AnimeTitle(
                english=anime["title"],
                japanese=anime["original_title"],
                romaji=anime["original_title_romanised"],
            ),
            _description=anime["description"],
            _director=anime["director"],
            _producer=anime["producer"],
            _release_date=int(anime["release_date"]),
            _running_time=int(anime["running_time"]),
            _rt_score=int(anime["rt_score"]),
            _people=anime["people"],
            _species=anime["species"],
            _locations=anime["locations"],
            _vehicles=anime["vehicles"],
        )

    def get_people(self, limit: int = 50) -> typing.List[Person]:
        """
        Get all people. This is limited to 50 by default (Also 50 in the API if the param is not
        provided).
        """

        response = requests.get(f"{self.endpoint}/people", params={"limit": limit})

        if response.status_code != 200:
            raise exceptions.ServerError(response)

        return [
            Person(
                _url=person["url"],
                _name=person.get("name"),
                _gender=person.get("gender"),
                _age=person.get("age"),
                _eye_color=person.get("eye_color"),
                _hair_color=person.get("hair_color"),
                _animes=person.get("films"),
                _species=person.get("species"),
            ) for person in response.json()
        ]

    def get_person(self, person_id: str) -> Person:
        """
        Get a person by its ID
        """

        response = requests.get(f"{self.endpoint}/people/{person_id}")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        person = response.json()

        return Person(
            _url=person["url"],
            _name=person.get("name"),
            _gender=person.get("gender"),
            _age=person.get("age"),
            _eye_color=person.get("eye_color"),
            _hair_color=person.get("hair_color"),
            _animes=person.get("films"),
            _species=person.get("species"),
        )

    def get_locations(self, limit: int = 50) -> typing.List[Location]:
        """
        Get all locations. This is limited to 50 by default (Also 50 in the API if the param is not
        provided).
        """

        response = requests.get(f"{self.endpoint}/locations", params={"limit": limit})

        if response.status_code != 200:
            raise exceptions.ServerError(response)

        return [
            Location(
                _url=location["url"],
                _name=location.get("name"),
                _climate=location.get("climate"),
                _terrain=location.get("terrain"),
                _surface_water=location.get("surface_water"),
                _residents=location.get("residents"),
                _animes=location.get("films"),
            ) for location in response.json()
        ]

    def get_location(self, location_id: str) -> Location:
        """
        Get location by ID
        """

        response = requests.get(f"{self.endpoint}/locations/{location_id}")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        location = response.json()

        return Location(
            _url=location["url"],
            _name=location.get("name"),
            _climate=location.get("climate"),
            _terrain=location.get("terrain"),
            _surface_water=location.get("surface_water"),
            _residents=location.get("residents"),
            _animes=location.get("films"),
        )

    def get_species(self, limit: int = 50) -> typing.List[Species]:
        """
        Get all species. This is limited to 50 by default (Also 50 in the API if the param is not
        provided).
        """

        response = requests.get(f"{self.endpoint}/species", params={"limit": limit})

        if response.status_code != 200:
            raise exceptions.ServerError(response)

        return [
            Species(
                _url=species["url"],
                _name=species.get("name"),
                _classification=species.get("classification"),
                _eye_colors=species.get("eye_colors"),
                _hair_colors=species.get("hair_colors"),
                _people=species.get("people"),
                _animes=species.get("films"),
            ) for species in response.json()
        ]

    def get_single_species(self, species_id: str) -> Species:
        """
        Get specie by ID
        """

        response = requests.get(f"{self.endpoint}/species/{species_id}")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        species = response.json()

        return Species(
            _url=species["url"],
            _name=species.get("name"),
            _classification=species.get("classification"),
            _eye_colors=species.get("eye_colors"),
            _hair_colors=species.get("hair_colors"),
            _people=species.get("people"),
            _animes=species.get("films"),
        )

    def get_vehicles(self, limit: int = 50) -> typing.List[Vehicle]:
        """
        Get all vehicles. This is limited to 50 by default (Also 50 in the API if the param is not
        provided).
        """

        response = requests.get(f"{self.endpoint}/vehicles", params={"limit": limit})

        if response.status_code != 200:
            raise exceptions.ServerError(response)

        return [
            Vehicle(
                _url=vehicle["url"],
                _name=vehicle.get("name"),
                _description=vehicle.get("description"),
                _vehicle_class=vehicle.get("vehicle_class"),
                _length=vehicle.get("length"),
                _pilot=vehicle.get("pilot"),
                _animes=vehicle.get("films"),
            ) for vehicle in response.json()
        ]

    def get_vehicle(self, vehicle_id: str) -> Vehicle:
        """
        Get vehicle by ID
        """

        response = requests.get(f"{self.endpoint}/vehicles/{vehicle_id}")

        if response.status_code != 200:
            raise exceptions.ServerError(status_code=response.status_code)

        vehicle = response.json()

        return Vehicle(
            _url=vehicle["url"],
            _name=vehicle.get("name"),
            _description=vehicle.get("description"),
            _vehicle_class=vehicle.get("vehicle_class"),
            _length=vehicle.get("length"),
            _pilot=vehicle.get("pilot"),
            _animes=vehicle.get("films"),
        )
