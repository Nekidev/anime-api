# The Anime API Project

All API wrappers can be imported from `anime_api.apis`. For example, the Anime Facts Rest API's wrapper class can be imported from `anime_api.apis.anime_facts_rest_api` or directly from `anime_api.apis`.

- [Nekos API](#nekos-api)
- [Anime Facts Rest API](#anime-facts-rest-api)
- [Trace.moe API](#tracemoe-api)
- [Animechan API](#animechan-api)
- [Waifu.pics API](#waifupics-api)
- [Studio Ghibli API](#studio-ghibli-api)
- [Kyoko API](#kyoko-api)
- [Animu API](#animu-api)
- [Nekos.life API](#nekoslife-api)
- [NekoBot API](#nekobot-api)
- [Neko-Love API](#neko-love-api)
- [Nekos.moe API](#nekosmoe-api)
- [Nekos.best](#nekosbest)
- [Waifu.im](#waifuim-api)

## Installation

Using pip:

```bash
pip install anime-api
```

Using Poetry:

```bash
poetry add anime-api
```

### List of all API wrappers

A list of all planned or available API wrappers can be imported from `anime_api`.

```python3
from anime_api import api_list
```

The list contains a `tuple` with 4 items for each API. For each `api` in the list, `api[0]` is the API name, `api[1]` is the wrapper class (or `None` if not available), `api[2]` is the documentation URL, and `api[3]` is a boolean that will be true or false depending of the availability of the API (`True` if available, otherwise `False`).

## Nekos API

Nekos API is an actively developed free open-source anime images API that serves anime images. The project is mantained by [Nekidev](https://github.com/Nekidev) and the source code can be found in it's [GitHub repository](https://github.com/Nekidev/nekos-api). You can [join the Discord server](https://discord.gg/PgQnuM3YnM) for more info, support and more.

The Nekos API wrapper is in the `anime_api.apis` module.

```python3
from anime_api.apis import NekosAPI

# If you own an access token, you can use it with the `token` argument.
api = NekosAPI()
```

The wrapper handles ratelimiting by itself. The API's rate limit is currently 1 request per second. If you call two or more methods without waiting a second, the wrappper will sleep until a new request can be made. For example:

```python3
import time

from anime_api.apis import NekosAPI


api = NekosAPI()

# First call, runs normally
api.get_random_image()

# Has not waited and will be ratelimmited. To prevent this, the wrapper will
# wait 1 second to make a new request.
api.get_image_by_id(image_id="some-uuid-v4")

# This simulates some processing your program makes that takes half a second.
time.sleep(.5)

# A new request is made but, as the previous request was made less than a
# second ago, the wrapper will wait the missing 500 milliseconds to make the
# request.
api.get_category_by_id(category_id="some-uuid-v4")
```

### `get_random_image(categories: Optional[list] = None)`

The `get_random_image` method returns an `anime_api.apis.nekos_api.objects.Image` object.

```python3
from anime_api.apis import NekosAPI

api = NekosAPI()

image = api.get_random_image(categories=["kemonomimi"])
```

### The `Image` class

The `Image` class contains all the information about an image returned from the API. It has the following properties:

- `id`: (`str`) The image's ID.
- `url`: (`str`) The image's URL.
- `artist`: (`Optional[Artist]`) The image's artist.
- `source`: (`Optional[_Source]`) The image's source (original post).
  - `name`: (`str`) The name of the website where it was first posted.
  - `url`: (`str`) The link to the original post.
- `original`: (`Optional[bool]`) Wether the image is drawn by the original author or is a fan art.
- `nsfw`: (`NsfwLevel`) The image's nsfw level. This property is an `Enum` and can be one of the following:
  - `NsfwLevel.UNKNOWN`: The nsfw level is unknown (not yet added by the API admins). This level should be considered as NSFW since it may contain this type of content.
  - `NsfwLevel.SFW`: Completely SFW and for all ages.
  - `NsfwLevel.QUESTIONABLE`: Ecchi content. Not explicit, but suggestive.
  - `NsfwLevel.NSFW`: Not Safe For Work. Not explicit, but borderline.
- `categories`: (`List[Category]`) A list of the image categories.
- `characters`: (`List[Character]`) A list of all characters that appear in the image.
- `created_at`: (`datetime.datetime`) The date and time when the image was added to the API.
- `etag`: (`str`) Useful for caching when requesting the image file.
- `size`: (`int`) The image file size in bytes.
- `mimetype`: (`str`) The image file's format.
- `color`: (`str`) The dominant color in the image in HEX. (i.e. #a0f4c3)
- `expires`: (`datetime.datetime`) The date and time when the image url expires. Image urls are signed so the expire an hour after requested.
- `dimens`: (`_Dimens`) The image dimensions. It has the following properties:
  - `height`: (`int`) The image's height.
  - `width`: (`int`) The image's width.
  - `aspect_ratio`: (`str`) The image's aspect ratio. (i.e. 2:3, 1:2, 16:9)
  - `orientation`: (`ImageOrientation`) This property is an Enum which has 3 possible values:
    - `ImageOrientation.LANDSCAPE`: The image's width is bigger than it's height.
    - `ImageOrientation.PORTRAIT`: The image's height is bigger than it's width.
    - `ImageOrientation.SQUARE`: The image's height is the same as it's width.
  
### `get_random_images(categories: Optional[list] = None, limit: int = 10)`

The `get_random_images` method works exactly the same as the `get_random_image` method, but instead or returning a single image, it returns a list of them. You can specify how many images will be returned with the `limit` argument (max 25).

```python3
from anime_api.apis import NekosAPI

api = NekosAPI()

images = api.get_random_images(categories=["catgirl"])

for image in images:
  print(image.url)
```

### `get_image_by_id(image_id: str)`

The `get_image_by_id` method returns an `Image` object with the specified ID.

```python3
from anime_api.apis import NekosAPI

api = NekosAPI()

image = api.get_image_by_id(image_id="some-uuid-v4")

print(image.url)
```

IDs identify each image. Take into account that the API ToS do not allow data storage for more than an hour. This means that you cannot store image IDs or any other type of data in your database or any other kind of data storage.

### `get_artist_by_id(artist_id: str)`

The `get_artist_by_id` method returns the information for the specified artist.

```python3
from anime_api.apis import NekosAPI

api = NekosAPI()

artist = api.get_artist_by_id(artist_id="some-uuid-v4)

print(artist.name)
```

This method returns an `anime_api.apis.nekos_api.objects.Artist` object.

### The `Artist` class.

The `Artist` class represents an illustrator which has images in the API. It has the following properties:

- `id`: (`str`) The artist's ID.
- `name`: (`str`) The artist's name.
- `url`: (`Optional[str]`) A link to the artist's official website/social media account.
- `images`: (`Optional[int]`) The amount of images uploaded to the API. This property is only present when fetching the artist by ID.

## Anime Facts Rest API

The Anime Facts Rest API is an API written in Node.js to get anime facts. The project is mantained by [Chadan-02](https://github.com/chandan-02) and the API documentation can be found [here](https://chandan-02.github.io/anime-facts-rest-api/).

The Anime Facts Rest API wrapper is in the `anime_api.apis` module.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestApi()
```

### `get_animes()`

The `get_animes` method returns a list of `anime_api.apis.anime_facts_rest_api.objects.Anime` objects.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestAPI()

animes = api.get_animes()
```

### The `Anime` class

The `Anime` class has 3 parameters: `id`, `name`, and `image`.

You can also get all its facts with the `facts()` method.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestAPI()

animes = api.get_animes()
anime = animes[0]
facts = anime.facts(api)
```

### The `Fact` class

The `Fact` object has 2 parameters: `id` and `fact`. Take into account that, although the official API says the `id` is the fact's ID, it seems to be the number of the fact in the response.

### `get_anime_facts(anime_name: str)`

You can fetch all facts for an anime using the `get_anime_facts` method. It will return a list of `Fact` objects.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestAPI()

facts = api.get_anime_facts(anime_name="bleach")
```

### `get_fact(anime_name: str, fact_id: int)`

The `get_fact()` method needs 2 arguments: `anime_name` and `fact_id`. This method returns a `Fact`.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestAPI()

fact = api.get_fact(anime_name="fma_brotherhood", fact_id=1)
```

## Trace.moe API

The Trace.moe API is an API to search for anime scenes from screenshots. The API documentation can be found [here](https://soruly.github.io/trace.moe/#/).

The Trace.moe API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import TraceMoeAPI

api = TraceMoeAPI()
```

### `search(file: File, get_anime_info: bool = True, cut_black_borders: bool = False)`

The Trace.moe API wrapper has only 1 method. This method is used to get the anime scene from where the screenshot was taken. You will need to pass the screenshot either as a bytes object with its `content_type` (`image/png`, `image/jpeg`, `video/mp4`, etc.), or a URL string (no `content_type` required).

With a url:

```python3
from anime_api.apis import TraceMoeAPI
from anime_api.apis.trace_moe_api import File

api = TraceMoeAPI()

result = api.search(file=File(url="https://i.imgur.com/1ZQ3Z4A.png"))
```

With a bytes object:

```python3
from anime_api.apis import TraceMoeAPI
from anime_api.apis.trace_moe_api import File

api = TraceMoeAPI()

with open("screenshot.png", "rb") as f:
    result = api.search(file=File(file=f.read(), content_type="image/png"))
```

The `result` variable will be a `anime_api.apis.trace_moe_api.objects.Result` object.

The `search()` method has 2 extra (optional) parameters: `get_anime_info` (defaults to `True`) and `cut_black_borders` (defaults to `False`). If the `cut_black_borders` is set to `True`, the screenshot will be cropped to remove the black borders (this is done by the API).

### The `Result` class

The `Result` class represents a match for the screenshot.

Parameters:

- `anime`: `anime_api.apis.trace_moe_api.objects.Anime` object.
- `filename`: The filename of the screenshot.
- `episode`: The episode number.
- `from_`: The start time of the scene. (has an underscore at the end because `from` is a reserved word in Python)
- `to`: The end time of the scene.
- `similarity`: The similarity of the screenshot to the scene.
- `video`: The URL of the mathcing video. (if any)
- `image`: The URL of the matching screenshot.

### The `Anime` class

The `Anime` class represents the anime of the scene.

Parameters:

- `anilist_id`: The AniList ID of the anime.
- `mal_id`: The MyAnimeList ID of the anime.
- `title`: An class with the anime's title in different languages.
  - `title.romaji`: The anime's romanized title.
  - `title.synonyms`: A list of the anime's synonyms.
  - `title.english`: The anime's english title.
  - `title.native`: The anime's native title.
- `is_adult`: A boolean that will be `True` if the anime is for adults, otherwise `False`.

If the `get_anime_info` was set to `False` when calling the `search()` method, all the `anime` parameters will be `None` except for `anilist_id`.

## Animechan API

The Animechan API is an API to get anime quotes. The API documentation can be found [here](https://animechan.vercel.app/).

The Animechan API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import AnimechanAPI

api = AnimechanAPI()
```

### `get_random_quote()`

The `get_random_quote()` method returns a `anime_api.apis.animechan_api.objects.Quote` object.

```python3
from anime_api.apis import AnimechanAPI

api = AnimechanAPI()

quote = api.get_random_quote()
```

### `get_many_random_quotes()`

The `get_many_random_quotes()` method returns a list of 10 `anime_api.apis.animechan_api.objects.Quote` objects.

```python3
from anime_api.apis import AnimechanAPI

api = AnimechanAPI()

quotes = api.get_many_random_quotes()
```

### `search_by_anime_title(anime_title: str, page: int = 1)`

The `search_by_anime_title()` method returns a list of `anime_api.apis.animechan_api.objects.Quote` objects. The `anime_title` parameter is the title of the anime you want to search for. The `page` parameter is the page number of the results (defaults to 1).

```python3
from anime_api.apis import AnimechanAPI

api = AnimechanAPI()

quotes = api.search_by_anime_title(anime_title="naruto")
```

### `search_by_character_name(character_name: str, page: int = 1)`

The `search_by_character_name()` method returns a list of `anime_api.apis.animechan_api.objects.Quote` objects. The `character_name` parameter is the name of the character you want to search for. The `page` parameter is the page number of the results (defaults to 1).

```python3
from anime_api.apis import AnimechanAPI

api = AnimechanAPI()

quotes = api.search_by_character_name(character_name="naruto")
```

### `get_animes()`

The `get_animes()` method returns a list of strings. Each item is an anime title.

```python3
from anime_api.apis import AnimechanAPI

api = AnimechanAPI()

animes = api.get_animes()
```

## Waifu.pics API

The Waifu.pics API is an API to get anime images. The API documentation can be found [here](https://waifu.pics/docs).

The Waifu.pics API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import WaifuPicsAPI

api = WaifuPicsAPI()
```

### `get_random_image(category: ImageCategory.SFW | ImageCategory.NSFW)`

The `get_random_image()` method returns a `anime_api.apis.waifu_pics_api.objects.Image` object. The `category` parameter is the category of the image you want to get. It can be any value of `ImageCategory.SFW` or `ImageCategory.NSFW`.

```python3
from anime_api.apis import WaifuPicsAPI
from anime_api.apis.waifu_pics_api.types import ImageCategory

api = WaifuPicsAPI()

image = api.get_random_image(category=ImageCategory.SFW.WAIFU)
```

The `image` variable will be a `anime_api.apis.waifu_pics_api.objects.Image` object. This has a `url` parameter which is the URL of the image.

### The `ImageCategory` class

The `ImageCategory` class has 2 sub-classes `SFW` and `NSFW`. Each subclass is an `enum.Enum`.

`SFW` categories:

- `WAIFU`
- `NEKO`
- `SHINOBU`
- `MEGUMIN`
- `BULLY`
- `CUDDLE`
- `CRY`
- `HUG`
- `AWOO`
- `KISS`
- `LICK`
- `PAT`
- `SMUG`
- `BONK`
- `YEET`
- `BLUSH`
- `SMILE`
- `WAVE`
- `HIGHFIVE`
- `HANDHOLD`
- `NOM`
- `BITE`
- `GLARE`
- `SLAP`
- `KILL`
- `KICK`
- `HAPPY`
- `WINK`
- `POKE`
- `DANCE`
- `CRINGE`

`NSFW` categories:

_The NSFW properties return content +18. The names contain obscene content and therefore won't be listed. You can find them at `anime_api/apis/waifu_pics/types.py`_

### `get_many_random_images(category: ImageCategory.SFW | ImageCategory.NSFW, exclude: list[str | Image] = [])`

The `get_many_random_images()` method returns a list of 30 `anime_api.apis.waifu_pics_api.objects.Image` objects. The `category` parameter is the same as in `get_random_image()`.

```python3
from anime_api.apis import WaifuPicsAPI
from anime_api.apis.waifu_pics_api.types import ImageCategory

api = WaifuPicsAPI()

images = api.get_many_random_images(category=ImageCategory.SFW.WAIFU)
```

This method also has an `exclude` parameter. This parameter is a list of strings or `anime_api.apis.waifu_pics_api.objects.Image` objects. If you want to exclude an image from the results, you can add the URL of the image to the `exclude` list.

```python3
from anime_api.apis import WaifuPicsAPI
from anime_api.apis.waifu_pics_api.types import ImageCategory

api = WaifuPicsAPI()

images = api.get_many_random_images(
  category=ImageCategory.SFW.WAIFU,
  exclude=[
    "https://example.com/img.png",
    Image(url="https://example.com/other-img.png")
  ]
)
```

_The URL strings and the Image objects can be combined in the `exclude` list._

This parameter can be useful to get a list of images without duplicates.

```python3
from anime_api.apis import WaifuPicsAPI
from anime_api.apis.waifu_pics_api.types import ImageCategory

api = WaifuPicsAPI()

images1 = api.get_many_random_images(category=ImageCategory.SFW.WAIFU)
images2 = api.get_many_random_images(category=ImageCategory.SFW.WAIFU, exclude=images1)

images_list = images1 + images2
```

## Studio Ghibli API

The Studio Ghibli API is an API to get information about Studio Ghibli movies. The API documentation can be found [here](https://ghibliapi.herokuapp.com/).

The Studio Ghibli API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()
```

This API wrapper, unlike the other API wrappers, object relationships will be loaded dynamically. This is because the API returns a list of urls for the relationships. This means that if, for example, you want to get all the people in an anime, when you call `anime.people` you will get a list of unloaded objects. These will automatically be loaded when you access their attributes.

For example:

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

# Returns a loaded Anime object
anime = api.get_anime(anime_id="2baf70d1-42bb-4437-b551-e5fed5a87abe")

# Returns a list of unloaded Person objects
people = anime.people

# Still unloaded
first_person = people[0]

# Loads the person object. You will notice a delay here (the connection to the API is made).
people.name

# The object was already loaded, so there is no delay.
people.eye_color
```

### `get_animes()`

The `get_animes()` method returns a list of `anime_api.apis.studio_ghibli_api.objects.Anime` objects.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

animes = api.get_animes()
```

### `get_anime(anime_id: str)`

The `get_anime()` method returns a `anime_api.apis.studio_ghibli_api.objects.Anime` object. The `anime_id` parameter is the ID of the anime you want to get.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

anime = api.get_anime(anime_id="2baf70d1-42bb-4437-b551-e5fed5a87abe")
```

### The `Anime` class

The anime class supports dynamic loading of relationships. This means that if you want to get the people in an anime, you will get a list of unloaded objects. These will automatically be loaded when you access their attributes.

The `Anime` class has the following attributes:

- `id: str` (uuid)
- `title: _AnimeTitle`
  - `title.english: str`
  - `title.japanese: str`
  - `title.romaji: str`
- `description: str`
- `director: str`
- `producer: str`
- `release_date: str`
- `rt_score: int`
- `running_time: int`
- `people: list[Person]` (loads dynamically)
- `species: list[Species]` (loads dynamically)
- `locations: list[Location]` (loads dynamically)
- `vehicles: list[Vehicle]` (loads dynamically)

### `get_people()`

The `get_people()` method returns a list of `anime_api.apis.studio_ghibli_api.objects.Person` objects.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

people = api.get_people()
```

### `get_person(person_id: str)`

The `get_person()` method returns a `anime_api.apis.studio_ghibli_api.objects.Person` object. The `person_id` parameter is the ID of the person you want to get.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

person = api.get_person(person_id="ba924631-068e-4436-b6de-f3283fa848f0")
```

### The `Person` class

\*Dynamic loading of relationships: **Yes\***

The `Person` class has the following attributes:

- `id: str` (uuid)
- `name: str`
- `gender: str`
- `age: str`
- `eye_color: str`
- `hair_color: str`
- `animes: list[Anime]` (loads dynamically)
- `species: Species` (loads dynamically)

### `get_species()`

The `get_species()` method returns a list of `anime_api.apis.studio_ghibli_api.objects.Species` objects.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

species = api.get_species()
```

### `get_single_species(species_id: str)`

The `get_single_species()` method returns a `anime_api.apis.studio_ghibli_api.objects.Species` object. The `species_id` parameter is the ID of the species you want to get.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

species = api.get_single_species(species_id="af3910a6-429f-4c74-9ad5-dfe1c4aa04f4")
```

_(Note: because species is singular and plural, the method had to be renamed to `get_single_species`)_

### The `Species` class

\*Dynamic loading of relationships: **Yes\***

The `Species` class has the following attributes:

- `id: str` (uuid)
- `name: str`
- `classification: str`
- `eye_colors: str`
- `hair_colors: str`
- `people: list[Person]` (loads dynamically)
- `animes: list[Anime]` (loads dynamically)

### `get_locations()`

The `get_locations()` method returns a list of `anime_api.apis.studio_ghibli_api.objects.Location` objects.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

locations = api.get_locations()
```

### `get_location(location_id: str)`

The `get_location()` method returns a `anime_api.apis.studio_ghibli_api.objects.Location` object. The `location_id` parameter is the ID of the location you want to get.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

location = api.get_location(location_id="c491755a-407d-4d6e-b58a-240ec78b5063")
```

### The `Location` class

\*Dynamic loading of relationships: **Yes\***

The `Location` class has the following attributes:

- `id: str` (uuid)
- `name: str`
- `climate: str`
- `terrain: str`
- `surface_water: str`
- `residents: list[Person]` (loads dynamically)
- `animes: list[Anime]` (loads dynamically)

### `get_vehicles()`

The `get_vehicles()` method returns a list of `anime_api.apis.studio_ghibli_api.objects.Vehicle` objects.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

vehicles = api.get_vehicles()
```

### `get_vehicle(vehicle_id: str)`

The `get_vehicle()` method returns a `anime_api.apis.studio_ghibli_api.objects.Vehicle` object. The `vehicle_id` parameter is the ID of the vehicle you want to get.

```python3
from anime_api.apis import StudioGhibliAPI

api = StudioGhibliAPI()

vehicle = api.get_vehicle(vehicle_id="f25fa661-3073-414d-968a-34e18709c560")
```

### The `Vehicle` class

\*Dynamic loading of relationships: **Yes\***

The `Vehicle` class has the following attributes:

- `id: str` (uuid)
- `name: str`
- `description: str`
- `vehicle_class: str`
- `length: str`
- `pilot: Person` (loads dynamically)
- `animes: list[Anime]` (loads dynamically)

## Kyoko API

The Kyoko API is an API to get anime images and quotes. The API documentation can be found [here](https://github.com/Elliottophellia/kyoko).

The Kyoko API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import KyokoAPI

api = KyokoAPI()
```

### `get_random_quote()`

The `get_random_quote()` method returns a `anime_api.apis.kyoko_api.objects.Quote` object.

```python3
from anime_api.apis import KyokoAPI

api = KyokoAPI()

quote = api.get_random_quote()
```

### The `Quote` class

The `Quote` class has 4 parameters:

- `anime`: The anime title.
- `character`: The character name.
- `quote`: The quote.
- `id`: The quote ID.

### `get_random_slap()`

The `get_random_slap()` method returns a `anime_api.apis.kyoko_api.objects.Image` object.

```python3
from anime_api.apis import KyokoAPI

api = KyokoAPI()

image = api.get_random_slap()
```

The `image` variable will be a `anime_api.apis.kyoko_api.objects.Image` object. This has a `url` parameter which is the URL of the image.

### `get_random_kiss()`

The `get_random_kiss()` method returns a `anime_api.apis.kyoko_api.objects.Image` object.

```python3
from anime_api.apis import KyokoAPI

api = KyokoAPI()

image = api.get_random_kiss()
```

### `get_random_hug()`

The `get_random_hug()` method returns a `anime_api.apis.kyoko_api.objects.Image` object.

```python3
from anime_api.apis import KyokoAPI

api = KyokoAPI()

image = api.get_random_hug()
```

## Animu API

The Animu API is an API to get random anime gifs, facts, waifus and passwords (haha... wtf its true?).

The Animu API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import AnimuAPI

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)
```

This API requires an API token. It is free while you keep in their Discord server.

### How to get an API token

1. Join the official [Discord server](https://discord.gg/yyW389c).
2. Go to the `#bot-commands` channel.
3. Type `-claim` and wait for the bot to respond.
4. Go to your DMs.
5. Send your email to the bot
6. Copy your API token

Note that if you leave the Discord server, your API token will be revoked.

### `get_random_image(category: ImageCategory)`

The `get_random_image()` method returns a `anime_api.apis.animu_api.objects.Image` object. The `category` parameter is the category of the image you want to get.

```python3
from anime_api.apis import AnimuAPI
from anime_api.apis.animu.types import ImageType

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

image: Image = api.get_random_image(category=ImageType.YES)
```

The `ImageType` enum has the following values:

- `ANGRY`
- `BAKA`
- `BITE`
- `BLUSH`
- `BONK`
- `BORED`
- `BULLY`
- `BYE`
- `CHASE`
- `CHEER`
- `CRINGE`
- `CRY`
- `CUDDLE`
- `DAB`
- `DANCE`
- `DIE`
- `DISGUST`
- `FACEPALM`
- `FEED`
- `GLOMP`
- `HAPPY`
- `HI`
- `HIGHFIVE`
- `HOLD`
- `HUG`
- `KICK`
- `KILL`
- `KISS`
- `LAUGH`
- `LICK`
- `LOVE`
- `LURK`
- `MIDFING`
- `NERVOUS`
- `NOPE`
- `NOM`
- `NUZZLE`
- `PANIC`
- `PAT`
- `PECK`
- `POKE`
- `POUT`
- `PUNCH`
- `RUN`
- `SAD`
- `SHOOT`
- `SHRUG`
- `SIP`
- `SLAP`
- `SLEEPY`
- `SMILE`
- `SMUG`
- `STAB`
- `STARE`
- `SUICIDE`
- `TEASE`
- `THINK`
- `THUMBSUP`
- `TICKLE`
- `TRIGGERED`
- `WAG`
- `WAKE`
- `WINK`
- `YES`

### The `Image` class

The `Image` class has a `url` property which contains the url of the image.

### `get_random_quote()`

The `get_random_quote()` method returns a `anime_api.apis.animu_api.objects.Quote` object.

```python3
from anime_api.apis import AnimuAPI

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

quote: Quote = api.get_random_quote()
```

The `quote` variable will be a `anime_api.apis.animu_api.objects.Quote` object.

### The `Quote` class

The `Quote` class has 4 parameters:

- `anime`: The anime title.
- `character`: The character name.
- `quote`: The quote.
- `id`: The quote ID.

### `get_random_waifu()`

The `get_random_waifu()` method returns a `anime_api.apis.animu_api.objects.Waifu` object.

```python3
from anime_api.apis import AnimuAPI

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

waifu: Waifu = api.get_random_waifu()
```

The `waifu` variable will be a `anime_api.apis.animu_api.objects.Waifu` object.

### The `Waifu` class

The `Waifu` class has 5 parameters:

- `id`: The waifu ID.
- `name`: The waifu name.
  - `name.english`: The waifu name in english.
  - `name.japanese`: The waifu name in japanese.
  - `name.alternative`: The waifu name in alternative.
  - `name.romaji`: The waifu name in romaji (converted from `name.japanese`).
- `images`: A list of `Image` objects.
  - `images[0].url`: The url of the image.
- `from_`: The source from where the waifu is from.
  - `from_.name`: The name of the source.
  - `from_.type_`: The type of the source.
- `statistics`: The waifu statistics.
  - `statistics.favorites`: The number of favorites.
  - `statistics.love`: The amount of love ❤.
  - `statistics.hate`: The amount of hate 💔.
  - `statistics.upvotes`: The number of upvotes.
  - `statistics.downvotes`: The number of downvotes.

### `get_random_password()`

The `get_random_password()` method returns a string.

```python3
from anime_api.apis import AnimuAPI

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

password: str = api.get_random_password()
```

### `get_random_fact(tags: str | AND | OR, min_length: int | None = None, max_length: int | None = None)`

The `get_random_fact()` method returns a `anime_api.apis.animu_api.objects.Fact` object.

```python3
from anime_api.apis import AnimuAPI

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

fact: Fact = api.get_random_fact()
```

#### Operators

The `tags` parameter can be a string, `AND` or `OR`.

The `AND` operator will return a fact that has all the tags you specified. The `OR` operator will return a fact that has at least one of the tags you specified.

Usage:

```python3
from anime_api.apis import AnimuAPI
from anime_api.apis.animu.operators import AND, OR

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

fact1: Fact = api.get_random_fact(tags=AND("AttackOnTitan", "knife", "sword", ...))
fact2: Fact = api.get_random_fact(tags=OR("pokemon", "AttackOnTitan", "SwordArtOnline", ...))
fact3: Fact = api.get_random_fact(tags="pokemon")
```

### The `Fact` class

The `Fact` class has 3 parameters:

- `id`: The fact ID.
- `fact`: The fact.
- `tags`: A list of strings.

### `generate_random_password()`

The `generate_random_password()` method returns a string.

```python3
from anime_api.apis import AnimuAPI

api_token = "YOUR_API_TOKEN"

api = AnimuAPI(api_token=api_token)

password: str = api.generate_random_password()
```

## Hmtai

The Hmtai API is an API that returns random anime images, both SFW and NSFW. This can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import HmtaiAPI

api = HmtaiAPI()
```

### `get_random_image(category: ImageCategory.SFW | ImageCategory.NSFW)`

The `get_random_image()` method returns a `anime_api.apis.hmtai.objects.Image` object.

```python3
from anime_api.apis import HmtaiAPI
from anime_api.apis.hmtai.types import ImageCategory

api = HmtaiAPI()

image = api.get_random_image(category=ImageCategory.SFW.KISS)
```

The `image` variable will be a `anime_api.apis.hmtai.objects.Image` object. This has two parameters:

- `url`: The url of the image.
- `nsfw`: A boolean that indicates if the image is NSFW or not.

### The `ImageCategory` class

The `ImageCategory` class has 2 sub-classes:

- `SFW`: The SFW image categories.

  - `WAVE`
  - `WINK`
  - `TEA`
  - `BONK`
  - `PUNCH`
  - `POKE`
  - `BULLY`
  - `PAT`
  - `KISS`
  - `KICK`
  - `BLUSH`
  - `FEED`
  - `SMUG`
  - `HUG`
  - `CUDDLE`
  - `CRY`
  - `CRINGE`
  - `SLAP`
  - `FIVE`
  - `GLOMP`
  - `HAPPY`
  - `HOLD`
  - `NOM`
  - `SMILE`
  - `THROW`
  - `LICK`
  - `BITE`
  - `DANCE`
  - `BOOP`
  - `SLEEP`
  - `LIKE`
  - `KILL`
  - `TICKLE`
  - `NOSEBLEED`
  - `THREATEN`
  - `DEPRESSION`
  - `WOLF`
  - `JAHY`
  - `NEKO`
  - `COFFEE_ARTS`
  - `WALLPAPER`
  - `MOBILEWALLPAPER`

- `NSFW`: The NSFW image categories.
  - `RANDOM`: A random NSFW image category.

_The NSFW properties return content +18. The names contain obscene content and therefore won't be listed. You can find them at `anime_api/apis/hmtai/types.py`_

## Nekos.life API

The Nekos.life API is an API that returns random anime images. NSFW content was removed from the API some time ago so everything is SFW. The API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()
```

### `get_random_image(category: ImageCategory)`

The `get_random_image()` method returns a `anime_api.apis.nekos_life.objects.Image` object.

```python3
from anime_api.apis import NekosLifeAPI
from anime_api.apis.nekos_life.types import ImageCategory

api = NekosLifeAPI()

image = api.get_random_image(category=ImageCategory.WAVE)
```

The `image` variable will be a `anime_api.apis.nekos_life.objects.Image` object. This has a single `url` parameter that contains the url of the image.

### The `ImageCategory` Enum

The `ImageCategory` enum has the following values:

- `SMUG`
- `WOOF`
- `GASM`
- `EIGHT_BALL`
- `GOOSE`
- `CUDDLE`
- `AVATAR`
- `SLAP`
- `PAT`
- `GECG`
- `FEED`
- `FOX_GIRL`
- `LIZARD`
- `NEKO`
- `HUG`
- `MEOW`
- `KISS`
- `WALLPAPER`
- `TICKLE`
- `SPANK`
- `WAIFU`
- `LEWD`
- `NGIF`

### `get_random_cat_emoji()`

The `get_random_cat_emoji()` returns a random cat text emoji (ex: `=^._.^=`).

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

emoji = api.get_random_cat_emoji()
```

### `get_random_fact()`

The `get_random_fact()` returns a random fact.

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

fact = api.get_random_fact()
```

The `fact` variable will be an `anime_api.apis.nekos_life.objects.Fact` object. This has a single `fact` parameter that contains the fact.

### `get_random_name()`

The `get_random_name()` returns a randomly generated name as a string.

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

name = api.get_random_name()
```

### `owoify(text: str)`

The `owoify()` method _owoifies_ a string. For example, `hello developer` becomes `hewwo devewopew`.

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

owoified_text = api.owoify("hello developer")
```

### `spoiler(text: str)`

The `spoiler()` method adds a spoiler tag to a string. For example, `hello developer` becomes `||hello developer||`.

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

spoilered_text = api.spoiler("hello developer")
```

### `get_random_why()`

The `get_random_why()` method returns a random `why` question (ex: Why did ... ?).

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

why = api.get_random_why()
```

### `get_eight_ball()`

The `get_eight_ball()` method returns a random answer from an 8-ball.

```python3
from anime_api.apis import NekosLifeAPI

api = NekosLifeAPI()

answer = api.get_eight_ball()
```

The `answer` variable will be an `anime_api.apis.nekos_life.objects.EightBall` object. This has a `answer` property that contains the answer. Aditionally, it has a `image` property that contains an `Image` object with the url of an 8ball showing the answer.

## NekoBot API

The NekoBot API is an API that returns random anime images. The API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import NekoBotAPI

api = NekoBotAPI()
```

If you have a donator API key, you can pass it to the `NekoBotAPI` object when initializing it.

```python3
from anime_api.apis import NekoBotAPI

api = NekoBotAPI(donator_api_key="YOUR_API_KEY")
```

### `get_random_image(category: ImageCategory)`

The `get_random_image()` method returns a `anime_api.apis.nekobot.objects.Image` object.

```python3
from anime_api.apis import NekoBotAPI

api = NekoBotAPI()

image = api.get_random_image(category=ImageCategory.WAVE)
```

The `image` variable will be a `anime_api.apis.nekobot.objects.Image` object. This has a single `url` parameter that contains the url of the image.

### The `ImageCategory` class

The `ImageCategory` class has the following sub-classes:

- `SFW`: The SFW image categories.
  - `KEMONOMIMI`
  - `KANNA`
  - `GAH`
  - `COFFEE`
  - `FOOD`
- `NSFW`: The NSFW image categories.
- `BOTH`: This categories can return SFW or suggestive images. These endpoints have been marked in a specific category because the age rating is not always clear. It should be treated as NSFW fr security reasons (and the API wrapper will do so).

_The NSFW and BOTH properties return content +18. The names contain obscene content and therefore won't be listed. You can find them at `anime_api/apis/nekobot/types.py`_

### `gerate_image(image_type: ImageGenType, **kwargs)`

The `generate_image()` method returns a `anime_api.apis.nekobot.objects.Image` object.

```python3
from anime_api.apis import NekoBotAPI

api = NekoBotAPI()

image = api.generate_image(image_type=ImageGenType.LOLICE, url="https://someimage.url")
```

This method is difficult to document because each image type has different parameters. You can find each type's parameter in the [official documentation](https://docs.nekobot.xyz/#image-generation-ddlc). The parameters required in each type need to be passed as keyword arguments.

For example, with `ImageGenType.SHIP` the code should look like this:

```python3
from anime_api.apis import NekoBotAPI

api = NekoBotAPI()

image = api.generate_image(image_type=ImageGenType.SHIP, url1="https://someimage.url", url2="https://someimage.url")
```

Each keyword parameter is the same as the query parameter name in the documentation.

## Neko-Love API

The Neko-Love API is an API that returns random anime images. The API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import NekoLoveAPI

api = NekoLoveAPI()
```

### `get_random_image(category: ImageCategory.NSFW | ImageCategory.SFW)`

The `get_random_image()` method returns a `anime_api.apis.neko_love.objects.Image` object.

```python3
from anime_api.apis import NekoLoveAPI

api = NekoLoveAPI()

image = api.get_random_image(category=ImageCategory.SFW.NEKO)
```

The `image` variable will be a `anime_api.apis.neko_love.objects.Image` object. This has a `url` parameter that contains the url of the image and a `nsfw` parameter indicating wether the image is NSFW or not.

### The `ImageCategory` class

The `ImageCategory` class has the following sub-classes:

- `SFW`
  - `NEKO`
  - `KITSUNE`
  - `HUG`
  - `PAT`
  - `WAIFU`
  - `CRY`
  - `KISS`
  - `SLAP`
  - `SMUG`
  - `PUNCH`
- `NSFW`

_The NSFW properties return content +18. The names contain obscene content and therefore won't be listed. You can find them (well this time is only one) at `anime_api/apis/neko_love/types.py`_

## Nekos.Moe API

The Nekos.Moe API is an API that returns random anime images. The API wrapper can be imported from the `anime_api.apis` module.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI()
```

### Authorization

You can log in to the API in two different ways:

Using your username and password:

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI(username="YOUR_USERNAME", password="YOUR_PASSWORD")
```

Using an existent API token:

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI(api_token="YOUR_API_TOKEN")
```

You can regenerate your API token at any time using the `regenerate_api_token()` method.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI(username="YOUR_USERNAME", password="YOUR_PASSWORD")

api.regenerate_api_token(username="YOUR_USERNAME", password="YOUR_PASSWORD")
```

If you do not pass the username and password to the `regenerate_api_token()` method, the API token will be regenerated and the API will be logged out.

### `get_user(user_id: str = "@me")`

The `get_user()` method returns a `anime_api.apis.nekos_moe.objects.User` object.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI()

user = api.get_user()
```

If no argument is passed, the method will return the user that is logged in. If you pass a user ID, the method will return the user with that ID.

### The `User` class

_Supports dynamic loading: **yes**_

The `User` class has the following attributes:

- `id`: (`str`) The user ID.
- `username`: (`str`) The user's username.
- `created_at`: (`datetime.datetime`) The date when the user was created.
- `favorites`: (`List[Image]`) A list of the user's favorite images.
- `favorites_received`: (`int`) The number of favorites the user has received.
- `likes`: (`List[Image]`) A list of the user's liked images.
- `likes_received`: (`int`) The number of likes the user has received.
- `roles`: (`List[str]`) A list of the user's roles.
- `saved_tags`: (`List[str]`) A list of the user's saved tags.
- `uploads`: (`int`) The number of images the user has uploaded.

### The `Image` class

Import path: `anime_api.apis.nekos_moe.objects.Image`

_Supports dynamic loading: **yes**_

The `Image` class has the following attributes:

- `id`: (`str`) The image ID.
- `url`: (`str`) The image URL.
- `created_at`: (`datetime.datetime`) The date when the image was created.
- `nsfw`: (`bool`) Whether the image is NSFW or not.
- `tags`: (`List[str]`) A list of the image's tags.
- `uploader`: (`User`) The user that uploaded the image.
- `favorites`: (`int | None`) The number of favorites the image has received.
- `likes`: (`int | None`) The number of likes the image has received.
- `approver`: (`User | None`) The user that approved the image.
- `artist`: (`str | None`) The image's artist name.
- `pending`: `bool` Whether the image is pending for approval or not.

### `search_users(query: str, limit: int = 20, offset: int = 0)`

The `search_users()` method returns a list of `User` object.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI()

users = api.search_users(query="username or id")
```

### `get_image(image_id: str)`

The `get_image()` method returns a `anime_api.apis.nekos_moe.objects.Image` object.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI()

image = api.get_image(image_id="JVnj8jkjN") # Thats an invalid ID
```

### `search_images(nsfw: bool | None = None, uploader: str | None = None, artist: str | None = None, tags: List[str] | None = None, sort: SearchSort | None = None, posted_before: datetime.datetime | None = None, posted_after: datetime.datetime = None, limit: int = 20, offset: int = 0)`

The `search_images()` method returns a list of `Image` object.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI()

images = api.search_images(nsfw=False, tags=["tag1", "tag2"])
```

The `anime_api.apis.nekos_moe.types.SearchSort` class has the following properties:

- `NEWEST`
- `OLDEST`
- `RELEVANCE`
- `LIKES`

### `get_random_images(count: int)`

The `get_random_images()` method returns a `anime_api.apis.nekos_moe.objects.Image` object.

```python3
from anime_api.apis import NekosMoeAPI

api = NekoBotAPI()

images = api.get_random_images(5)
```

### `upload_image(image: str | bytes, nsfw: bool, tags: List[str], artist: str)`

**WARNING: THIS METHOD HAS NOT BEEN TESTED BECAUSE I CANNOT UPLOAD AN IMAGE EVERY TIME I WANT TO RUN A TEST (I'LL GET BLOCKED FOR SPAMMING). PROCEED WITH PRECAUTION.**

The `upload_image()` method is used to upload an image to Nekos.moe. All arguments are required.

```python3
from anime_api.apis import NekosMoeAPI

api = NekosMoeAPI(username="YOUR_USERNAME", password="YOUR_PASSWORD")

image = api.upload_image(image="path/to/image.jpg", nsfw=False, tags=["tag1", "tag2"], artist="artist name")
```

This will return a `anime_api.apis.nekos_moe.objects.PendingImage` object.

### The `PendingImage` class

The `PendingImage` class has the following attributes:

- `image`: (`Image`) The image that was uploaded.
- `image_url`: (`str`) The image URL. This is the same as `image.url`.
- `post_url`: (`str`) The URL to the post on Nekos.moe.

## Nekos.best

The Nekos.best API is an API to get a variety of random (or not so random) anime images. The `NekosBest` class can be imported from `anime_api.apis`.

```python3
from anime_api.apis import NekosBest

api = NekosBest()
```

### `get_random_image(category: ImageCategory)`

The `get_random_image()` method returns a `anime_api.apis.nekos_best.objects.Image` object.

```python3
from anime_api.apis import NekosBest

api = NekosBest()

image = api.get_random_image(category=ImageCategory.ANIME)
```

The `anime_api.apis.nekos_best.types.ImageCategory` class has the following properties:

- `HIGHFIVE`
- `HAPPY`
- `SLEEP`
- `HANDHOLD`
- `LAUGH`
- `BITE`
- `POKE`
- `TICKLE`
- `KISS`
- `WAVE`
- `THUMBSUP`
- `STARE`
- `CUDDLE`
- `SMILE`
- `BAKA`
- `BLUSH`
- `THINK`
- `POUT`
- `FACEPALM`
- `WINK`
- `SHOOT`
- `SMUG`
- `PAT`
- `PUNCH`
- `DANCE`
- `FEED`
- `SHRUG`
- `BORED`
- `KICK`
- `HUG`
- `YEET`
- `SLAP`
- `NEKO`
- `HUSBANDO`
- `KITSUNE`
- `WAIFU`

### The `Image` class

The `Image` class has the following attributes:

- `url`: (`str`) The image URL.
- `artist`: (`Artist | None`)
  - `artist.name`: (`str`) The artist's name.
  - `artist.url`: (`str`) The artist's URL.
- `anime`: (`Anime | None`)
  - `anime.title`: (`str`) The anime's title.
- `source_url`: (`str | None`) The source URL of the image.

### `search_images(query: str, image_category: ImageCategory | None = None, image_type: ImageType | None = None, amount: int = 1)`

The `search_images()` method returns a list of `Image` object.

```python3
from anime_api.apis import NekosBest
from anime_api.apis.nekos_best.types import ImageCategory, ImageType

api = NekosBest()

images = api.search_images(query="cute neko", image_category=ImageCategory.NEKO, image_type=ImageType.GIF, amount=5)
```

The `anime_api.apis.nekos_best.types.ImageType` class has the following properties:

- `IMAGE`: Return only static images
- `GIF`: Return only GIFs


# Waifu.im API

The Waifu.im API is a public API to get a variety of random (or not so random) anime images. The `WaifuIm` class can be imported from `anime_api.apis`.

```python3
from anime_api.apis import WaifuImAPI

api = WaifuImAPI()
```

### `get_random_image(
  tags: typing.Optional[
    typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
  ] = None,
  excluded_tags: typing.Optional[
    typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
  ] = None,
  selected_file: typing.Optional[str] = None,
  excluded_files: typing.Optional[typing.List[str]] = None,
  is_nsfw: typing.Optional[bool] = None,
  is_gif: bool = False,
  order_by: typing.Optional[SearchSort] = SearchSort.RANDOM,
  orientation: typing.Optional[ImageOrientation] = None,
)`

The `get_random_image()` method returns a `anime_api.apis.waifu_im.objects.Image` object.

```python3
from anime_api.apis import WaifuImAPI
from anime_api.apis.waifu_im.types import ImageTag, SearchSort, ImageOrientation

api = WaifuImAPI()

image = api.get_random_image(
  tags=[ImageTag.SFW.WAIFU],
  excluded_tags=[ImageTag.SFW.MAID],
  excluded_files=["some-image-signature"],
  is_nsfw=False,
  is_gif=False,
  order_by=SearchSort.RANDOM,
  orientation=ImageOrientation.LANDSCAPE,
)

print(image.url)
```

The `anime_api.apis.waifu_im.types.ImageTag` class has the following properties:

#### SFW

- `MAID`
- `WAIFU`
- `MARIN_KITAGAWA`
- `MORI_CALLIOPE`
- `RAIDEN_SHOGUN`
- `OPPAI`
- `SELFIES`
- `UNIFORM`

_The NSFW properties return content +18. The names contain obscene content and therefore won't be listed. You can find them at `anime_api/apis/waifu_im/types.py`_

### The `Image` class

The `Image` class has the following attributes:

- `id`: (`str`) The image ID.
- `signature`: (`str`) The image signature.
- `extension`: (`str`) The image extension.
- `favorites`: (`int`) The amount of favorites the image has.
- `dominant_color`: (`str`) The dominant color of the image.
- `source`: (`str`) The source of the image.
- `uploaded_at`: (`datetime.datetime`) The date the image was uploaded.
- `is_nsfw`: (`bool`) Whether the image is NSFW or not.
- `dimens`: (`Dimens`)
  - `dimens.width`: (`int`) The image width.
  - `dimens.height`: (`int`) The image height.
- `url`: (`str`) The image URL.
- `preview_url`: (`str`) The image preview URL.
- `tags`: (`typing.List[ImageTag]`)

### `get_many_random_images(
  tags: typing.Optional[
    typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
  ] = None,
  excluded_tags: typing.Optional[
    typing.List[typing.Union[ImageTag.SFW, ImageTag.NSFW]]
  ] = None,
  included_files: typing.Optional[typing.List[str]] = None,
  excluded_files: typing.Optional[typing.List[str]] = None,
  is_nsfw: typing.Optional[bool] = None,
  is_gif: bool = False,
  order_by: typing.Optional[SearchSort] = SearchSort.RANDOM,
  orientation: typing.Optional[ImageOrientation] = None,
)`

The `get_many_random_images()` method returns a list of 30 `anime_api.apis.waifu_im.objects.Image` objects.

```python3
from anime_api.apis import WaifuImAPI
from anime_api.apis.waifu_im.types import ImageTag, SearchSort, ImageOrientation

api = WaifuImAPI()

images = api.get_many_random_images(
  tags=[ImageTag.SFW.WAIFU],
  excluded_tags=[ImageTag.SFW.MAID],
  excluded_files=["some-image-signature"],
  is_nsfw=False,
  is_gif=False,
  order_by=SearchSort.RANDOM,
  orientation=ImageOrientation.LANDSCAPE,
)

for image in images:
  print(image.url)
```

**Endpoints that require authorization have not yet been implemented.**