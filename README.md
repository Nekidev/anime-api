# The Anime API Project

[![ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/G2G6I3GT1) [![Coinbase](https://img.shields.io/badge/Coinbase-0052FF?style=for-the-badge&logo=Coinbase&logoColor=white)](https://nyekipy.cb.id)

The Anime API is a collection of wrappers for different types of free anime-related APIs. [Join our Discord server](https://discord.gg/PgQnuM3YnM).

## Why anime-api (and not others)?

There are several reasons why would you prefer using anime-api:

-   **Intuitive**: anime-api is designed to be intuitive. Supports autocompletion everywhere.
-   **Typed**: Wrappers expose Python objects for provider responses.
-   **Simple**: Get all the anime information you want with a single line of code.
-   **Legal**: I shouldn't need to say this, but all the APIs are legal. (no free streaming services/others)
-   **Provider status**: See the dated audit below before choosing a wrapper.

## Installation

Using Poetry:

```
poetry add anime-api
```

Using pip:

```
pip install anime-api
```

## Documentation

The full documentation can be found [here](https://github.com/Nekidev/anime-api/tree/main/docs).

## Provider directory

Links were checked on **October 14, 2026**. A reachable documentation page does
not establish API uptime or wrapper compatibility. `api_list` lists included
wrappers, not a live health check. See [provider status and migrations](docs/provider-status.md)
for retired services, uncertain results, and replacement choices.

| Provider | Documentation | Wrapper / status |
| --- | --- | --- |
| Animechan v1 | [Docs](https://animechan.io/docs) | `AnimechanV1API`: random quotes and filters; live JSON verified |
| Trace.moe | [Docs](https://soruly.github.io/trace.moe-api/) | `TraceMoeAPI`; docs reachable |
| Waifu.pics | [Docs](https://waifu.pics/docs) | `WaifuPicsAPI`; docs reachable |
| Studio Ghibli | [Docs](https://ghibliapi.dev/) | `StudioGhibliAPI`; moved from Heroku |
| Nekos.best | [Docs](https://docs.nekos.best/) | `NekosBest`; docs reachable |
| Nekos.moe | [Docs](https://docs.nekos.moe/) | `NekosMoeAPI`; docs reachable |
| Nekos.life | [Source / docs](https://github.com/Nekos-life/nekos.py) | `NekosLifeAPI`; source reachable |
| NekoBot | [Docs](https://docs.nekobot.xyz/) | `NekoBotAPI`; docs reachable |
| Waifu.im | [Docs](https://docs.waifu.im/) | `WaifuImAPI`; current contract needs review |
| Animu / Waifu.it | See provider status | `AnimuAPI`; host unverified |
| Hmtai | See provider status | `HmtaiAPI`; host unverified |
| Neko-Love | See provider status | `NekoLoveAPI`; host unverified |
| Kitsu | [Docs](https://kitsu.docs.apiary.io/) | No wrapper |
| AniList | [Docs](https://anilist.gitbook.io/anilist-apiv2-docs/) | No wrapper |
| AniDB | See provider status | No wrapper; docs access blocked |
| Anime News Network | [Docs](https://www.animenewsnetwork.com/encyclopedia/api.php) | No wrapper |
| Notify.moe | [Docs](https://notify.moe/api) | No wrapper |
| Shikimori | [Docs](https://shikimori.one/api/doc) | No wrapper |
| MangaDex | [Docs](https://api.mangadex.org/docs/) | No wrapper; corrected docs URL |
| Danbooru | [Docs](https://danbooru.donmai.us/wiki_pages/help:api) | No wrapper |
| Yandere | [Docs](https://yande.re/help/api) | No wrapper |
| Konachan | [Docs](https://konachan.com/help/api) | No wrapper |
| Anime Character Database | [Docs](http://wiki.animecharactersdatabase.com/index.php?title=API_Access) | No wrapper |
| Jikan | [Source](https://github.com/jikan-me/jikan-rest) | Self-hosted only; public service discontinued |
| Jikan-Edge (new alternative) | [Docs](https://jikan.lucashdo.com/) | External API; sample JSON verified; no wrapper; different response schema |
| Tenrai (new alternative) | [Docs](https://tenrai.org/) | Docs reachable; sample API request failed; no wrapper |

### Current quote client

Install this checkout with `python -m pip install -e .` to use the new client.
The published PyPI release does not include this maintenance change yet.

```python
from anime_api.apis import AnimechanV1API

api = AnimechanV1API(timeout=10)
quote = api.get_random_quote()  # One network request
print(quote.quote, quote.character, quote.anime)
# Optional: api.get_random_quote(anime_title="Naruto")
```

The new client supports random quotes only, including anime or character filters.
It uses the current nested response format and preserves the existing `Quote`
dataclass. No key is needed for the free tier; check provider limits before use.
Legacy `AnimechanAPI` targets a parked domain: migrate to `AnimechanV1API`.

### Recheck links

```powershell
python scripts/check_links.py --output link-audit.json
```

The dependency-free checker scans tracked Markdown, Python, TOML and workflow
files, follows redirects, bounds request time, and saves status codes and file
locations. It flags 404/410 responses and detected parking pages. Authentication,
bot blocks, DNS errors and timeouts stay **unverified**; inspect them before
removing a provider. An API base path can return 404 while its resource routes work.

### Development

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e . pytest
.venv/Scripts/python.exe -m pytest tests/test_animechan_v1.py tests/test_link_checker.py
```

Most existing tests call live third-party services. Run those explicitly when you
have service access; the tests above run offline.

## Contributing

Read the following before contributing:

### Adding an API

If you want to add an API to the list, please make sure that:

-   The API is free to use
-   The API is anime-related (or manga-related)
-   You follow the same architecture as the other API wrappers
-   Document the code you write
-   Add all the necessary tests to the `tests` folder

### Fixing an API wrapper

Before fixing an API wrapper, please make sure that:

-   The bug is not being fixed in another PR
-   The bug is actually a bug and not a feature (xd)
-   The bug is not a bug from the API itself
-   You have created an issue. If you have not created an issue, please create one before fixing the bug.

### Requesting a new API

If you want to request a new API, please make sure that:

-   The API is free to use
-   The API is anime-related (or manga-related)
-   It is not already in the list (wether available or not)

Once you have checked this, please create an issue with the following information:

-   The name of the API
-   The API docs link
-   List of all the features the API has

## Maintainers

<table>
  <tr>
    <td style="align:center;">
      <a href="https://github.com/Nekidev">
        <img src="https://avatars.githubusercontent.com/u/84998222?s=256&v=4" height="100" width="100" alt="Nekidev avatar" />
        <br>
        <span>Nekidev</span>
      </a>
    </td>
  </tr>
</table>
