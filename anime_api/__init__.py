"""
This file contains a list of all the available or planned apis.
"""
from anime_api import apis


# List of tuples (api_name, api_class, api_docs_url, is_available)
api_list = [
    (
        "Anime Facts Rest API",
        apis.AnimeFactsRestAPI,
        "https://chandan-02.github.io/anime-facts-rest-api/",
        True,
    ),
    (
        "Trace.moe API",
        apis.TraceMoeAPI,
        "https://soruly.github.io/trace.moe-api/",
        True,
    ),
    ("Animechan", apis.AnimechanAPI, "https://animechan.vercel.app/docs", True),
    ("Jikan", None, "https://jikan.docs.apiary.io/#", False),
    ("Waifu Pics", apis.WaifuPicsAPI, "https://waifu.pics/docs", True),
    ("Studio Ghibli API", apis.StudioGhibliAPI, "https://ghibliapi.herokuapp.com/", True),
    ("Kitsu", None, "https://kitsu.docs.apiary.io/#", False),
    ("AniList", None, "https://anilist.gitbook.io/anilist-apiv2-docs/", False),
    ("AniDB", None, "https://wiki.anidb.net/w/API", False),
    ("Kyoko", apis.KyokoAPI, "https://github.com/Elliottophellia/kyoko", True),
    ("Animu", apis.AnimuAPI, "https://docs.animu.ml/", True),
    ("AniSearch", None, "https://anisearch.com/developers", False),
    (
        "Anime News Network",
        None,
        "https://www.animenewsnetwork.com/encyclopedia/api.php",
        False,
    ),
    ("Notify.moe", None, "https://notify.moe/api", False),
    ("Hmtai", apis.HmtaiAPI, "https://hmtai.herokuapp.com/endpoints", True),
    ("Nekos.life", None, "https://github.com/Nekos-life/nekos.py", False),
    ("NekoBot", apis.NekoBotAPI, "https://docs.nekobot.xyz/", True),
    ("Neko-love", apis.NekoLoveAPI, "https://docs.neko-love.xyz/", True),
    ("Nekos.moe", apis.NekosMoeAPI, "https://docs.nekos.moe/", True),
    ("Nekos.best", apis.NekosBest, "https://docs.nekos.best/", True),
    ("Shikimori", None, "https://shikimori.one/api/doc", False),
    ("Mangadex", None, "https://api.mangadex.org/docs.html", False),
    ("Danbooru", None, "https://danbooru.donmai.us/wiki_pages/help:api", False),
    (
        "Yandere",
        None,
        "https://yande.re/help/api",
        False,
    ),  # Yandere and Konachan are forks of the same github repo. That's why they have almost-identical apis.
    ("Konachan", None, "https://konachan.com/help/api", False),
    ("Waifu.im", apis.WaifuImAPI, "https://waifu.im/", True),
    ("Catboys", apis.CatboysAPI, "https://catboys.com/api", True),
    (
        "Anime Character Database",
        None,
        "http://wiki.animecharactersdatabase.com/index.php?title=API_Access",
        False,
    ),
    (
        "Nekos API",
        apis.NekosAPI,
        "https://nekos.nekidev.com/docs/rest-api/endpoints",
        True,
    ),
]

__version__ = '0.15.0'
__authors__ = ['Nekidev <neki@nekidev.com>']
__license__ = "MIT License"
