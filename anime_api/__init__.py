"""
This file contains a list of all the available or planned apis.
"""
from anime_api.apis.anime_facts_rest_api import AnimeFactsRestAPI
from anime_api.apis.trace_moe import TraceMoeAPI
from anime_api.apis.animechan import AnimechanAPI
from anime_api.apis.waifu_pics import WaifuPicsAPI
from anime_api.apis.studio_ghibli_api import StudioGhibliAPI


# List of tuples (api_name, api_class, api_docs_url, is_available)
api_list = [
    (
        "Anime Facts Rest API",
        AnimeFactsRestAPI,
        "https://chandan-02.github.io/anime-facts-rest-api/",
        True,
    ),
    (
        "Trace.moe API",
        TraceMoeAPI,
        "https://soruly.github.io/trace.moe-api/",
        True,
    ),
    ("Animechan", AnimechanAPI, "https://animechan.vercel.app/guide", True),
    ("Jikan", None, "https://jikan.docs.apiary.io/#", False),
    ("Waifu Pics", WaifuPicsAPI, "https://waifu.pics/docs", True),
    ("Studio Ghibli API", StudioGhibliAPI, "https://ghibliapi.herokuapp.com/", True),
    ("Kitsu", None, "https://kitsu.docs.apiary.io/#", False),
    ("AniList", None, "https://anilist.gitbook.io/anilist-apiv2-docs/", False),
    ("AniDB", None, "https://wiki.anidb.net/w/API", False),
    ("Kyoko", None, "https://github.com/Elliottophellia/kyoko", False),
    ("Animu", None, "https://docs.animu.ml/", False),
    ("AniSearch", None, "https://anisearch.com/developers", False),
    (
        "Anime News Network",
        None,
        "https://www.animenewsnetwork.com/encyclopedia/api.php",
        False,
    ),
    ("Notify.moe", None, "https://notify.moe/api", False),
    ("Hmtai", None, "https://hmtai.herokuapp.com/endpoints", False),
    ("Nekos.life", None, "https://github.com/Nekos-life/nekos.py", False),
    ("NekoBot", None, "https://docs.nekobot.xyz/", False),
    ("Neko-love", None, "https://docs.neko-love.xyz/", False),
    ("Nekos.moe", None, "https://docs.nekos.moe/", False),
    ("Nekos.best", None, "https://docs.nekos.best/", False),
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
    ("Waifu.im", None, "https://waifu.im/", False),
    ("Catboys", None, "https://catboys.com/api", False),
]
