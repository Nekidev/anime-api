# The Anime API Project

All API wrappers can be imported from `anime_api.apis`. For example, the Anime Facts Rest API's wrapper class can be imported from `anime_api.apis.anime_facts_rest_api` or directly from `anime_api.apis`.

- [Anime Facts Rest API](#anime-facts-rest-api)
- [Trace.moe API](#tracemoe-api)
- [Animechan API](#animechan-api)
- [Waifu.pics API](#waifupics-api)
- [Studio Ghibli API](#studio-ghibli-api)
- [Kyoko API](#kyoko-api)


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

- `WAIFU`
- `NEKO`
- `TRAP`
- `BLOWJOB`


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

*The URL strings and the Image objects can be combined in the `exclude` list.*

This parameter can be useful to get a list of images without duplicates.

```python3
from anime_api.apis import WaifuPicsAPI
from anime_api.apis.waifu_pics_api.types import ImageCategory

api = WaifuPicsAPI()

images1 = api.get_many_random_images(category=ImageCategory.SFW.WAIFU)
images2 = api.get_many_random_images(category=ImageCategory.SFW.WAIFU, exclude=images1)

images_list = images1 + images2
```


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
