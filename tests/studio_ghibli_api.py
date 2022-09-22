"""
Run tests for the StudioGhibliAPI class.

Usage:
    cd tests
    poetry run python -m pytest studio_ghibli_api.py
"""
from anime_api.apis import StudioGhibliAPI
from anime_api.apis.studio_ghibli_api.objects import Anime, Person, Location, Species, Vehicle


def test_get_animes():
    """
    Test the get_animes method
    """
    api = StudioGhibliAPI()
    animes = api.get_animes()

    assert isinstance(animes, list)
    assert len(animes) > 0
    for anime in animes:
        assert isinstance(anime, Anime), f"{anime} is not an Anime object"


def test_get_anime():
    """
    Test the get_anime method
    """
    api = StudioGhibliAPI()
    anime = api.get_anime("2baf70d1-42bb-4437-b551-e5fed5a87abe")

    assert isinstance(anime, Anime)
    assert anime.is_loaded
    assert isinstance(anime.people, list)
    assert isinstance(anime.people[0], Person)
    assert isinstance(anime.locations, list)
    assert isinstance(anime.locations[0], Location)
    assert isinstance(anime.species, list)
    assert isinstance(anime.species[0], Species)
    assert isinstance(anime.vehicles, list)
    assert isinstance(anime.vehicles[0], Vehicle)


def test_dynamic_anime_loading():
    """
    Test the dynamic loading of an anime
    """
    anime = Anime(
        _url="https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
    )
    assert not anime.is_loaded
    assert anime.load()
    assert anime.is_loaded
    assert anime.description
    assert isinstance(anime.people, list)
    assert isinstance(anime.people[0], Person)
    assert isinstance(anime.locations, list)
    assert isinstance(anime.locations[0], Location)
    assert isinstance(anime.species, list)
    assert isinstance(anime.species[0], Species)
    assert isinstance(anime.vehicles, list)
    assert isinstance(anime.vehicles[0], Vehicle)


def test_get_people():
    """
    Test the get_people method
    """
    api = StudioGhibliAPI()
    people = api.get_people()

    assert isinstance(people, list)
    assert len(people) > 0
    for person in people:
        assert isinstance(person, Person), f"{person} is not a Person object"


def test_get_person():
    """
    Test the get_person method
    """
    api = StudioGhibliAPI()
    person = api.get_person("ba924631-068e-4436-b6de-f3283fa848f0")

    assert isinstance(person, Person)
    assert person.is_loaded
    assert isinstance(person.animes, list)
    assert isinstance(person.animes[0], Anime)
    assert isinstance(person.species, Species)


def test_dynamic_person_loading():
    """
    Test the dynamic loading of a person
    """
    person = Person(
        _url="https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"
    )
    assert not person.is_loaded
    assert person.load()
    assert person.is_loaded
    assert person.name
    assert isinstance(person.animes, list)
    assert isinstance(person.animes[0], Anime)
    assert isinstance(person.species, Species)


def test_get_locations():
    """
    Test the get_locations method
    """
    api = StudioGhibliAPI()
    locations = api.get_locations()

    assert isinstance(locations, list)
    assert len(locations) > 0
    for location in locations:
        assert isinstance(location, Location), f"{location} is not a Location object"


def test_get_location():
    """
    Test the get_location method
    """
    api = StudioGhibliAPI()
    location = api.get_location("11014596-71b0-4b3e-b8c0-1c4b15f28b9a")

    assert isinstance(location, Location)
    assert location.is_loaded
    assert isinstance(location.residents, list)
    assert isinstance(location.residents[0], Person)
    assert isinstance(location.animes, list)
    assert isinstance(location.animes[0], Anime)


def test_dynamic_location_loading():
    """
    Test the dynamic loading of a location
    """
    location = Location(
        _url="https://ghibliapi.herokuapp.com/locations/11014596-71b0-4b3e-b8c0-1c4b15f28b9a"
    )
    assert not location.is_loaded
    assert location.load()
    assert location.is_loaded
    assert location.name
    assert isinstance(location.residents, list)
    assert isinstance(location.residents[0], Person)
    assert isinstance(location.animes, list)
    assert isinstance(location.animes[0], Anime)


def test_get_species():
    """
    Test the get_species method
    """
    api = StudioGhibliAPI()
    species = api.get_species()

    assert isinstance(species, list)
    assert len(species) > 0
    for species in species:
        assert isinstance(species, Species), f"{species} is not a Species object"


def test_get_single_species():
    """
    Test the get_specie method
    """
    api = StudioGhibliAPI()
    species = api.get_single_species("af3910a6-429f-4c74-9ad5-dfe1c4aa04f2")

    assert isinstance(species, Species)
    assert species.is_loaded
    assert isinstance(species.people, list)
    assert isinstance(species.people[0], Person)
    assert isinstance(species.animes, list)
    assert isinstance(species.animes[0], Anime)


def test_dynamic_species_loading():
    """
    Test the dynamic loading of a species
    """
    species = Species(
        _url="https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
    )
    assert not species.is_loaded
    assert species.load()
    assert species.is_loaded
    assert species.name
    assert isinstance(species.people, list)
    assert isinstance(species.people[0], Person)
    assert isinstance(species.animes, list)
    assert isinstance(species.animes[0], Anime)


def test_get_vehicles():
    """
    Test the get_vehicles method
    """
    api = StudioGhibliAPI()
    vehicles = api.get_vehicles()

    assert isinstance(vehicles, list)
    assert len(vehicles) > 0
    for vehicle in vehicles:
        assert isinstance(vehicle, Vehicle), f"{vehicle} is not a Vehicle object"


def test_get_vehicle():
    """
    Test the get_vehicle method
    """
    api = StudioGhibliAPI()
    vehicle = api.get_vehicle("4e09b023-f650-4747-9ab9-eacf14540cfb")

    assert isinstance(vehicle, Vehicle)
    assert vehicle.is_loaded
    assert isinstance(vehicle.pilot, Person)
    assert isinstance(vehicle.animes, list)
    assert isinstance(vehicle.animes[0], Anime)


def test_dynamic_vehicle_loading():
    """
    Test the dynamic loading of a vehicle
    """
    vehicle = Vehicle(
        _url="https://ghibliapi.herokuapp.com/vehicles/4e09b023-f650-4747-9ab9-eacf14540cfb"
    )
    assert not vehicle.is_loaded
    assert vehicle.load()
    assert vehicle.is_loaded
    assert vehicle.name
    assert isinstance(vehicle.pilot, Person)
    assert isinstance(vehicle.animes, list)
    assert isinstance(vehicle.animes[0], Anime)
