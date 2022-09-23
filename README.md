
![Loli count](https://count.getloli.com/get/@anime-api?theme=gelbooru)

The Anime API is a collection of wrappers for different types of free anime-related APIs.


## Why anime-api (and not others)?

There are several reasons why would you prefer using anime-api:
- **Intuitive**: anime-api is designed to be intuitive. Supports autocompletion everywhere.
- **Complete**: Every actively supported API has no feature left apart.
- **Simple**: Get all the anime information you want with a single line of code.
- **Legal**: I shouldn't need to say this, but all the APIs are legal. (no free streaming services/others)
- **Actively supported**: Get new releases (with new API wrappers) every now and then.


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

The full documentation can be found [here](https://nekidev.github.io/anime-api/docs/).


## APIs

These are the currently supported and planned to add support for APIs:

| Name                        | API Documentation                                                                   | Available |
|-----------------------------|-------------------------------------------------------------------------------------|-----------|
| Anime Facts Rest API        | [Documentation](https://chandan-02.github.io/anime-facts-rest-api/)                 | ✅        |
| Trace.moe                   | [Documentation](https://soruly.github.io/trace.moe-api/)                            | ✅        |
| Animechan                   | [Documentation](https://animechan.vercel.app/guide)                                 | ✅        |
| Jikan (MyAnimeList)         | [Documentation](https://jikan.docs.apiary.io/)                                      | ❌        |
| Waifu Pics                  | [Documentation](https://waifu.pics/docs)                                            | ✅        |
| Studio Ghibli API           | [Documentation](https://ghibliapi.herokuapp.com/)                                   | ✅        |
| Kitsu                       | [Documentation](https://kitsu.docs.apiary.io/)                                      | ❌        |
| AniList                     | [Documentation](https://anilist.gitbook.io/anilist-apiv2-docs/)                     | ❌        |
| AniDB                       | [Documentation](https://wiki.anidb.net/w/API)                                       | ❌        |
| Kyoko                       | [Documentation](https://github.com/Elliottophellia/kyoko)                           | ✅        |
| Animu                       | [Documentation](https://docs.animu.ml/)                                             | ✅        |
| Anisearch                   | [Documentation](https://anisearch.com/developers)                                   | ❌        |
| Anime News Network          | [Documentation](https://www.animenewsnetwork.com/encyclopedia/api.php)              | ❌        |
| Notify.moe (Anime Notifier) | [Documentation](https://notify.moe/api)                                             | ❌        |
| Hmtai                       | [Documentation](https://hmtai.herokuapp.com/endpoints)                              | ✅        |
| Nekos.life                  | [Documentation](https://github.com/Nekos-life/nekos.py)                             | ✅        |
| NekoBot                     | [Documentation](https://docs.nekobot.xyz/)                                          | ❌        |
| Neko-Love                   | [Documentation](https://docs.neko-love.xyz/)                                        | ❌        |
| Nekos.best                  | [Documentation](https://docs.nekos.best/)                                           | ❌        |
| Nekos.moe                   | [Documentation](https://docs.nekos.moe/)                                            | ❌        |
| Shikimori                   | [Documentation](https://shikimori.one/api/doc)                                      | ❌        |
| MangaDex                    | [Documentation](https://api.mangadex.org/docs.html)                                 | ❌        |
| Danbooru                    | [Documentation](https://danbooru.donmai.us/wiki_pages/help:api)                     | ❌        |
| Yandere                     | [Documentation](https://yande.re/help/api)                                          | ❌        |
| Konachan                    | [Documentation](https://konachan.com/help/api)                                      | ❌        |
| Waifus.im                   | [Documentation](https://waifu.im/)                                                  | ❌        |
| Catboys                     | [Documentation](https://catboys.com/api)                                            | ❌        |
| Anime Character Database    | [Documentation](http://wiki.animecharactersdatabase.com/index.php?title=API_Access) | ❌        |


### APIs by feature

You know what you want to do, but have no idea of what API will work for you? This list orders the APIs by features. See which fits you best!


#### Images

- Animu:
  - Tons of anime gifs and images
  - Get reaction gifs from +60 different categories
  - Completely free
- Hmtai:
  - Tons of anime gifs and images
  - SFW and NSFW images
  - Get random images from +70 different categories
  - Completely free
- Nekos.life
  - Lots of different neko pics
  - Get random neko images from +20 different categories
  - Completely free
- Waifu.pics
  - Lots of different waifu images
  - Get random images from +30 categories
  - SFW and NSFW images
  - Get 30 different images with a single API call
  - Get a different image every time
  - Completely free


#### Facts

- Anime Facts Rest API:
  - Lots of different anime facts
  - Get random fact from an anime
  - Save fact ID and refetch the fact later
  - Get a list of all available animes
  - Completely free
- Animu:
  - Lots of anime facts
  - Get random anime facts
  - Completely free
- Kyoko:
  - Lots of different anime facts
  - Get random reaction gifs from 3 different categories
  - Completely free
- Nekos.life
  - Lots of different anime facts
  - Get random anime facts
  - Completely free


#### Quotes

- Animechan:
  - Lots of different quotes from a large list of characters and animes
  - Get random anime quotes
  - Get 10 random anime quotes with a single api call
  - Search quotes by character name or anime title
  - Get a list of all available animes
  - Completely free
- Animu:
  - Lots of different anime quotes with information about who said them and where
  - Get random anime quotes
  - Completely free.
- Kyoko:
  - Lots of different anime quotes
  - Get random quotes with information about who said them and where
  - Completely free


#### Waifus

- Animu:
  - Lots of different waifus from Video Games, Animes, Movies and more.
  - Get random waifus with their statistics, source, many images and more.
  - Completely free


#### Animes

- Anime Facts Rest API:
  - Get a list of lots of snake-case anime titles with their images and facts about them
  - Completely free
- Animechan:
  - Get a list of lots of anime titles with random quotes from them
  - Completely free
- Studio Ghibli API
  - Get Studio Ghibli animes with information such as director, producer, etc.
  - Dynamic loading support
  - Get super specific anime details such as veichles, locations, people, and species.
  - Completely free


#### Games

- Nekos.life
  - Get an answer from an 8ball with an aditional image of an 8ball showing the answer.
  - Get a random "why?" question
  - Completely free


#### Utilities

- Trace.moe
  - Find an anime from a screenshot with information about the specific anime, episode and time of the screenshot.
  - Completely free
- Nekos.life
  - Get a random cat text emoji
  - Generate random names
  - Owoify text (`hello` => `hewwo`)
  - Mark text as spoiler (`hello` => `||hello||`) (API endpoint is currently bugged)
  - Completely free
- Animu:
  - Generate a secure password
  - Completely free


### APIs that will not be supported
- Illegal anime streaming services
- Non anime-related APIs
- APIs that are not APIs (i.e. web scrapping)


## Contributing

Go ahead and make your pull request 🍴


## Mantainers
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
