# The Anime API Project

All API wrappers can be imported from `anime_api.apis`. For example, the Anime Facts Rest API's wrapper class can be imported from `anime_api.apis.anime_facts_rest_api` or directly from `anime_api.apis`.

- [Anime Facts Rest API](#anime-facts-rest-api)
- [Trace.moe API](#trace.moe-api)
- [Animechan API](#animechan-api)
- [Waifu.pics API](#waifu.pics-api)
- [Studio Ghibli API](#studio-ghibli-api)


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


### The `Anime` object

The `Anime` object has 3 parameters: `id`, `name`, and `image`.

You can also get all its facts with the `facts()` method.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestAPI()

animes = api.get_animes()
anime = animes[0]
facts = anime.facts(api)
```


### The `Fact` object

The `Fact` object has 2 parameters: `id` and `fact`. Take into account that, although the official API says the `id` is the fact's ID, it seems to be the number of the fact in the response.


### `get_anime_facts()`

You can fetch all facts for an anime using the `get_anime_facts` method. It will return a list of `Fact` objects.

```python3
from anime_api.apis import AnimeFactsRestAPI

api = AnimeFactsRestAPI()

facts = api.get_anime_facts(anime_name="bleach")
```


### `get_fact()`

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


### `search()`

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

### The `Result` object

The `Result` object represents a match for the screenshot.

Parameters:

- `anime`: `anime_api.apis.trace_moe_api.objects.Anime` object.
- `filename`: The filename of the screenshot.
- `episode`: The episode number.
- `from_`: The start time of the scene. (has an underscore at the end because `from` is a reserved word in Python)
- `to`: The end time of the scene.
- `similarity`: The similarity of the screenshot to the scene.
- `video`: The URL of the mathcing video. (if any)
- `image`: The URL of the matching screenshot.

### The `Anime` object

The `Anime` object represents the anime of the scene.

Parameters:

- `anilist_id`: The AniList ID of the anime.
- `mal_id`: The MyAnimeList ID of the anime.
- `title`: An object with the anime's title in different languages.
  - `title.romaji`: The anime's romanized title.
  - `title.synonyms`: A list of the anime's synonyms.
  - `title.english`: The anime's english title.
  - `title.native`: The anime's native title.
- `is_adult`: A boolean that will be `True` if the anime is for adults, otherwise `False`.

If the `get_anime_info` was set to `False` when calling the `search()` method, all the `anime` parameters will be `None` except for `anilist_id`.
