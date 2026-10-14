"""
This file contains a list of all the available or planned apis.
"""
from anime_api import apis


# Tuples: name, wrapper class, docs URL, wrapper included.
# Inclusion is not a service health guarantee. See docs/provider-status.md.
# Retired clients remain importable from anime_api.apis for compatibility.
api_list = [
    (
        "Trace.moe API",
        apis.TraceMoeAPI,
        "https://soruly.github.io/trace.moe-api/",
        True,
    ),
    ("Animechan v1 (random quotes)", apis.AnimechanV1API, "https://animechan.io/docs", True),
    ("Jikan (self-hosted)", None, "https://github.com/jikan-me/jikan-rest", False),
    ("Waifu Pics", apis.WaifuPicsAPI, "https://waifu.pics/docs", True),
    ("Studio Ghibli API", apis.StudioGhibliAPI, "https://ghibliapi.dev/", True),
    ("Jikan-Edge", None, "https://jikan.lucashdo.com/", False),
    ("Tenrai", None, "https://tenrai.org/", False),
    ("Kitsu", None, "https://kitsu.docs.apiary.io/#", False),
    ("AniList", None, "https://anilist.gitbook.io/anilist-apiv2-docs/", False),
    ("AniDB", None, "https://wiki.anidb.net/w/API", False),
    ("Animu", apis.AnimuAPI, "https://docs.waifu.it/", True),
    (
        "Anime News Network",
        None,
        "https://www.animenewsnetwork.com/encyclopedia/api.php",
        False,
    ),
    ("Notify.moe", None, "https://notify.moe/api", False),
    ("Hmtai", apis.HmtaiAPI, "https://hmtai.hatsunia.cfd/v2/endpoints", True),
    ("Nekos.life", apis.NekosLifeAPI, "https://github.com/Nekos-life/nekos.py", True),
    ("NekoBot", apis.NekoBotAPI, "https://docs.nekobot.xyz/", True),
    ("Neko-love", apis.NekoLoveAPI, "https://docs.neko-love.xyz/", True),
    ("Nekos.moe", apis.NekosMoeAPI, "https://docs.nekos.moe/", True),
    ("Nekos.best", apis.NekosBest, "https://docs.nekos.best/", True),
    ("Shikimori", None, "https://shikimori.one/api/doc", False),
    ("Mangadex", None, "https://api.mangadex.org/docs/", False),
    ("Danbooru", None, "https://danbooru.donmai.us/wiki_pages/help:api", False),
    (
        "Yandere",
        None,
        "https://yande.re/help/api",
        False,
    ),  # Yandere and Konachan are forks of the same github repo. That's why they have almost-identical apis.
    ("Konachan", None, "https://konachan.com/help/api", False),
    ("Waifu.im", apis.WaifuImAPI, "https://docs.waifu.im/", True),
    (
        "Anime Character Database",
        None,
        "http://wiki.animecharactersdatabase.com/index.php?title=API_Access",
        False,
    ),
]

__version__ = '1.0.2'
__authors__ = ['Nekidev <nyeki@nyeki.dev>']
__license__ = "MIT License"
