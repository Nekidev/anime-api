# The Anime API Project

All API wrappers can be imported from `anime_api.apis`. For example, the Anime Facts Rest API's wrapper class can be imported from `anime_api.apis.anime_facts_rest_api` or directly from `anime_api.apis`.

- [Anime Facts Rest API](#anime-facts-rest-api)
- [Trace.moe API](#trace-moe-api)
- [Animechan API](#animechan-api)


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

All API wrappers support using custom endpoints. You can change them by passing `endpoint` as a parameter when initializing the class.

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
