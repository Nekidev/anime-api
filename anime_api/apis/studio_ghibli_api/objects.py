import typing

from dataclasses import dataclass


@dataclass
class _AnimeTitle:
    english: str
    japanese: str
    romaji: str


@dataclass
class Anime:
    """
    Object representation of a film. Named Anime to keep it consistent with the
    rest of the API. The object can automatically load itself if you try to access
    any of the attributes (if not already loaded).
    """

    _url: str
    _people: typing.Iterable[str] = ()
    _is_people_loaded: bool = False
    _species: typing.Iterable[str] = ()
    _is_species_loaded: bool = False
    _locations: typing.Iterable[str] = ()
    _is_locations_loaded: bool = False
    _vehicles: typing.Iterable[str] = ()
    _is_vehicles_loaded: bool = False

    _title: typing.Optional[_AnimeTitle] = None
    _description: typing.Optional[str] = None
    _director: typing.Optional[str] = None
    _producer: typing.Optional[str] = None
    _release_date: typing.Optional[int] = None
    _running_time: typing.Optional[int] = None
    _rt_score: typing.Optional[int] = None

    @property
    def id(self) -> str:
        """
        Get the ID of the anime
        """
        return self._url.rsplit("/", maxsplit=1)[-1]

    def load(self) -> bool:
        """
        Load the anime
        """
        if self.is_loaded:
            return False

        from anime_api.apis import StudioGhibliAPI

        api = StudioGhibliAPI()
        anime = api.get_anime(anime_id=self.id)

        self._title = anime._title
        self._description = anime._description
        self._director = anime._director
        self._producer = anime._producer
        self._release_date = anime._release_date
        self._running_time = anime._running_time
        self._rt_score = anime._rt_score
        self._people = anime._people
        self._species = anime._species
        self._locations = anime._locations
        self._vehicles = anime._vehicles

        return True

    @property
    def is_loaded(self):
        """
        Check if the anime is loaded
        """
        if not self._description:
            return False
        return True

    @property
    def title(self) -> _AnimeTitle:
        """
        Get the title of the anime
        """
        if not self._title and not self.is_loaded:
            self.load()
        return self._title

    @property
    def description(self) -> str:
        """
        Get the description of the anime
        """
        if not self._description and not self.is_loaded:
            self.load()
        return self._description

    @property
    def director(self) -> str:
        """
        Get the director of the anime
        """
        if not self._director and not self.is_loaded:
            self.load()
        return self._director

    @property
    def producer(self) -> str:
        """
        Get the producer of the anime
        """
        if not self._producer and not self.is_loaded:
            self.load()
        return self._producer

    @property
    def release_date(self) -> int:
        """
        Get the release date of the anime
        """
        if not self._release_date and not self.is_loaded:
            self.load()
        return self._release_date

    @property
    def running_time(self) -> int:
        """
        Get the running time of the anime
        """
        if not self._running_time and not self.is_loaded:
            self.load()
        return self._running_time

    @property
    def rt_score(self) -> int:
        """
        Get the RT score of the anime
        """
        if not self._rt_score and not self.is_loaded:
            self.load()
        return self._rt_score

    @property
    def people(self) -> typing.List['Person']:
        """
        Get the people of the anime
        """
        if not self._people and not self.is_loaded:
            self.load()

        if not self._is_people_loaded:
            people_objects = []

            for person in self._people:
                people_objects.append(Person(_url=person))
            self._people = people_objects
            self._is_people_loaded = True

        return self._people

    @property
    def species(self) -> typing.List[str]:
        """
        Get the species of the anime
        """
        if not self._species and not self.is_loaded:
            self.load()
        
        if not self._is_species_loaded:
            species_objects = []

            for species in self._species:
                species_objects.append(Species(_url=species))
            self._species = species_objects
            self._is_species_loaded = True

        return self._species

    @property
    def locations(self) -> typing.List[str]:
        """
        Get the locations of the anime
        """
        if not self._locations and not self.is_loaded:
            self.load()

        if not self._is_locations_loaded:
            location_objects = []

            for location in self._locations:
                location_objects.append(Location(_url=location))
            self._locations = location_objects
            self._is_locations_loaded = True

        return self._locations

    @property
    def vehicles(self) -> typing.List[str]:
        """
        Get the vehicles of the anime
        """
        if not self._vehicles and not self.is_loaded:
            self.load()

        if not self._is_vehicles_loaded:
            vehicle_objects = []

            for vehicle in self._vehicles:
                vehicle_objects.append(Vehicle(_url=vehicle))
            self._vehicles = vehicle_objects
            self._is_vehicles_loaded = True

        return self._vehicles

    def __repr__(self):
        self.load()
        return self.title.english


@dataclass
class Person:
    """
    Object representation of a person. The object automatically loads itself (if not already 
    loaded) if you try to access any of the attributes.
    """

    _url: str
    _name: typing.Optional[str] = None
    _gender: typing.Optional[str] = None
    _age: typing.Optional[str] = None
    _eye_color: typing.Optional[str] = None
    _hair_color: typing.Optional[str] = None
    _animes: typing.Iterable[str] = ()
    _is_animes_loaded: bool = False
    _species: typing.Optional[str] = None
    _is_species_loaded: bool = False

    @property
    def id(self) -> str:
        """
        Get the ID of the person
        """
        return self._url.rsplit("/", maxsplit=1)[-1]

    @property
    def is_loaded(self) -> bool:
        """
        Check if the person is loaded
        """
        if not self._name:
            return False
        return True

    def load(self) -> bool:
        """
        Load the person
        """
        if self.is_loaded:
            return False

        from anime_api.apis import StudioGhibliAPI

        api = StudioGhibliAPI()
        person: Person = api.get_person(person_id=self.id)

        self._name = person._name
        self._gender = person._gender
        self._age = person._age
        self._eye_color = person._eye_color
        self._hair_color = person._hair_color
        self._animes = person._animes
        self._species = person._species

        return True

    @property
    def name(self) -> str:
        """
        Get the name of the person
        """
        if not self._name and not self.is_loaded:
            self.load()
        return self._name

    @property
    def gender(self) -> str:
        """
        Get the gender of the person
        """
        if not self._gender and not self.is_loaded:
            self.load()
        return self._gender

    @property
    def age(self) -> int:
        """
        Get the age of the person
        """
        if not self._age and not self.is_loaded:
            self.load()
        return self._age

    @property
    def eye_color(self) -> str:
        """
        Get the eye color of the person
        """
        if not self._eye_color and not self.is_loaded:
            self.load()
        return self._eye_color

    @property
    def hair_color(self) -> str:
        """
        Get the hair color of the person
        """
        if not self._hair_color and not self.is_loaded:
            self.load()
        return self._hair_color

    @property
    def animes(self) -> typing.List['Anime']:
        """
        Get the animes of the person
        """
        if not self._animes and not self.is_loaded:
            self.load()

        if not self._is_animes_loaded:
            anime_objects = []

            for anime in self._animes:
                anime_objects.append(Anime(_url=anime))
            self._animes = anime_objects
            self._is_animes_loaded = True

        return self._animes

    @property
    def species(self) -> str:
        """
        Get the species of the person
        """
        if not self._species and not self.is_loaded:
            self.load()

        if not self._is_species_loaded and self._species:
            self._species = Species(_url=self._species)
            self._is_species_loaded = True

        return self._species

    def __repr__(self):
        self.load()
        return self.name


@dataclass
class Location:
    """
    Object representation of a location. The object automatically loads itself (if not already 
    loaded) if you try to access any of the attributes.
    """

    _url: str
    _name: typing.Optional[str] = None
    _climate: typing.Optional[str] = None
    _terrain: typing.Optional[str] = None
    _surface_water: typing.Optional[str] = None
    _residents: typing.Iterable[typing.Union[str, Person]] = ()
    _is_residents_loaded: bool = False
    _animes: typing.Iterable[typing.Union[str, Anime]] = ()
    _is_animes_loaded: bool = False

    @property
    def id(self) -> str:
        """
        Get the ID of the location
        """
        return self._url.rsplit("/", maxsplit=1)[-1]

    @property
    def is_loaded(self) -> bool:
        """
        Check if the location is loaded
        """
        if not self._name:
            return False
        return True

    def load(self) -> bool:
        """
        Load the location
        """
        if self.is_loaded:
            return False

        from anime_api.apis import StudioGhibliAPI

        api = StudioGhibliAPI()
        location: Location = api.get_location(location_id=self.id)

        self._name = location._name
        self._climate = location._climate
        self._terrain = location._terrain
        self._surface_water = location._surface_water
        self._residents = location._residents
        self._animes = location._animes

        return True

    @property
    def name(self) -> str:
        """
        Get the name of the location
        """
        if not self._name and not self.is_loaded:
            self.load()
        return self._name

    @property
    def climate(self) -> str:
        """
        Get the climate of the location
        """
        if not self._climate and not self.is_loaded:
            self.load()
        return self._climate

    @property
    def terrain(self) -> str:
        """
        Get the terrain of the location
        """
        if not self._terrain and not self.is_loaded:
            self.load()
        return self._terrain

    @property
    def surface_water(self) -> int:
        """
        Get the surface water of the location
        """
        if not self._surface_water and not self.is_loaded:
            self.load()
        return self._surface_water

    @property
    def residents(self) -> typing.List[str]:
        """
        Get the residents of the location
        """
        if not self._residents and not self.is_loaded:
            self.load()

        if not self._is_residents_loaded:
            resident_objects = []

            for resident in self._residents:
                resident_objects.append(Person(_url=resident))

            self._residents = resident_objects
            self._is_residents_loaded = True

        return self._residents

    @property
    def animes(self) -> typing.List[str]:
        """
        Get the animes of the location
        """
        if not self._animes and not self.is_loaded:
            self.load()

        if not self._is_animes_loaded:
            anime_objects = []

            for anime in self._animes:
                anime_objects.append(Anime(_url=anime))

            self._animes = anime_objects
            self._is_animes_loaded = True

        return self._animes

    def __repr__(self):
        self.load()
        return self.name


@dataclass
class Species:
    """
    Object representation of a specie. The object automatically loads itself (if not already 
    loaded) if you try to access any of the attributes.
    """

    _url: str
    _name: typing.Optional[str] = None
    _classification: typing.Optional[str] = None
    _eye_colors: typing.Optional[str] = None
    _hair_colors: typing.Optional[str] = None
    _people: typing.Iterable[typing.Union[str, Person]] = ()
    _is_people_loaded: bool = False
    _animes: typing.Iterable[typing.Union[str, Anime]] = ()
    _is_animes_loaded: bool = False

    @property
    def id(self) -> str:
        """
        Get the ID of the specie
        """
        return self._url.rsplit("/", maxsplit=1)[-1]

    @property
    def is_loaded(self) -> bool:
        """
        Check if the specie is loaded
        """
        if not self._name:
            return False
        return True

    def load(self) -> bool:
        """
        Load the specie
        """
        if self.is_loaded:
            return False

        from anime_api.apis import StudioGhibliAPI

        api = StudioGhibliAPI()
        species: Species = api.get_single_species(species_id=self.id)

        self._name = species._name
        self._classification = species._classification
        self._eye_colors = species._eye_colors
        self._hair_colors = species._hair_colors
        self._people = species._people
        self._animes = species._animes

        return True

    @property
    def name(self) -> str:
        """
        Get the name of the specie
        """
        if not self._name and not self.is_loaded:
            self.load()
        return self._name

    @property
    def classification(self) -> str:
        """
        Get the classification of the specie
        """
        if not self._classification and not self.is_loaded:
            self.load()
        return self._classification

    @property
    def eye_colors(self) -> str:
        """
        Get the eye colors of the specie
        """
        if not self._eye_colors and not self.is_loaded:
            self.load()
        return self._eye_colors

    @property
    def hair_colors(self) -> str:
        """
        Get the hair colors of the specie
        """
        if not self._hair_colors and not self.is_loaded:
            self.load()
        return self._hair_colors

    @property
    def people(self) -> typing.List[str]:
        """
        Get the people of the specie
        """
        if not self._people and not self.is_loaded:
            self.load()

        if not self._is_people_loaded:
            people_objects = []

            for person in self._people:
                people_objects.append(Person(_url=person))

            self._people = people_objects
            self._is_people_loaded = True

        return self._people

    @property
    def animes(self) -> typing.List[Anime]:
        """
        Get the animes of the specie
        """
        if not self._animes and not self.is_loaded:
            self.load()

        if not self._is_animes_loaded:
            anime_objects = []

            for anime in self._animes:
                anime_objects.append(Anime(_url=anime))

            self._animes = anime_objects
            self._is_animes_loaded = True

        return self._animes

    def __repr__(self):
        self.load()
        return self.name


@dataclass
class Vehicle:
    """
    Object representation of a vehicle.
    """

    _url: str
    _name: typing.Optional[str] = None
    _description: typing.Optional[str] = None
    _vehicle_class: typing.Optional[str] = None
    _length: typing.Optional[str] = None
    _pilot: typing.Optional[typing.Union[str, Person]] = None
    _is_piolt_loaded: bool = False
    _animes: typing.Iterable[typing.Union[str, Anime]] = ()
    _is_animes_loaded: bool = False

    @property
    def id(self) -> str:
        """
        Get the ID of the vehicle
        """
        return self._url.rsplit("/", maxsplit=1)[-1]

    @property
    def is_loaded(self) -> bool:
        """
        Check if the vehicle is loaded
        """
        if not self._name:
            return False
        return True

    def load(self) -> bool:
        """
        Load the vehicle
        """
        if self.is_loaded:
            return False

        from anime_api.apis import StudioGhibliAPI

        api = StudioGhibliAPI()
        vehicle: Vehicle = api.get_vehicle(vehicle_id=self.id)

        self._name = vehicle._name
        self._description = vehicle._description
        self._vehicle_class = vehicle._vehicle_class
        self._length = vehicle._length
        self._pilot = vehicle._pilot
        self._animes = vehicle._animes

        return True

    @property
    def name(self) -> str:
        """
        Get the name of the vehicle
        """
        if not self._name and not self.is_loaded:
            self.load()
        return self._name

    @property
    def description(self) -> str:
        """
        Get the description of the vehicle
        """
        if not self._description and not self.is_loaded:
            self.load()
        return self._description

    @property
    def vehicle_class(self) -> str:
        """
        Get the vehicle class of the vehicle
        """
        if not self._vehicle_class and not self.is_loaded:
            self.load()
        return self._vehicle_class

    @property
    def length(self) -> str:
        """
        Get the length of the vehicle
        """
        if not self._length and not self.is_loaded:
            self.load()
        return self._length

    @property
    def pilot(self) -> typing.Optional[Person]:
        """
        Get the pilot of the vehicle
        """
        if not self._pilot and not self.is_loaded:
            self.load()

        if not self._is_piolt_loaded and self._pilot:
            self._pilot = Person(_url=self._pilot)
            self._is_piolt_loaded = True

        return self._pilot

    @property
    def animes(self) -> typing.List[Anime]:
        """
        Get the animes of the vehicle
        """
        if not self._animes and not self.is_loaded:
            self.load()

        if not self._is_animes_loaded:
            anime_objects = []

            for anime in self._animes:
                anime_objects.append(Anime(_url=anime))

            self._animes = anime_objects
            self._is_animes_loaded = True

        return self._animes
