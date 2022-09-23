import typing

from enum import Enum


class ImageGenType(Enum):
    """
    Image type for generation
    """

    THREATS = "threats"
    BAGUETTE = "baguette"
    CLYDE = "clyde"
    CAPTCHA = "captcha"
    WHO_WOULD_WIN = "whowouldwin"
    CHANGE_MY_MIND = "changemymind"
    DDLC = "ddlc"
    JPEG = "jpeg"
    LOLICE = "lolice"
    KANNA = "kannagen"
    IPHONE_X = "iphonex"
    KMS = "kms"
    ANIME_FACE = "animeface"
    AWOOIFY = "awooify"
    TRAP = "trap"
    NICHIJOU = "nichijou"
    TRUMP_TWEET = "trumptweet"
    TWEET = "tweet"
    KIDNAP = "kidnap"
    DEEPFRY = "deepfry"
    BLURPIFY = "blurpify"
    PHCOMMENT = "phcomment"
    MAGIK = "magik"
    OSU = "osu"
    CLICK_FOR_HENTAI = "clickforhentai"
    FACT = "fact"
    TRASH = "trash"
    STICKBUG = "stickbug"


class ImageCategory:
    """
    Image category
    """

    class SFW(Enum):
        """
        Safe For Work image types
        """

        KEMONOMIMI = "kemonomimi"
        KANNA = "kanna"
        GAH = "gah"
        COFFEE = "coffee"
        FOOD = "food"

    class NSFW(Enum):
        """
        Not Safe For Work (+18) image types
        """

        HENTAI_ASS = "hass"
        HENTAI_MIDRIFF = "midriff"
        PGIF = "pgif"
        FOUR_K = "4k"
        HENTAI = "hentai"
        HENTAI_NEKO = "hneko"
        HENTAI_KITSUNE = "hkitsune"
        ANAL = "anal"
        HENTAI_ANAL = "hanal"
        GONE_WILD = "gonewild"
        ASS = "ass"
        PUSSY = "pussy"
        THIGH = "thigh"
        HENTAI_THIGH = "hthigh"
        TENTACLE = "tentacle"
        BOOBS = "boobs"
        HENTAI_BOOBS = "hboobs"
        YAOI = "yaoi"
        PAIZURI = "paizuri"

        # Donator only. This image types have not been tested, so they were placed
        # in the NSFW category for security reasons (minors).
        COSPLAY = "cosplay"
        SWIMSUIT = "swimsuit"
        PANTSU = "pantsu"
        NAKADASHI = "nakadashi"

    class BOTH(Enum):
        """
        This image types can return either NSFW or SFW content. Should be considered as NSFW
        if the images are being displayed in a place minors have access to.
        """

        HOLO = "holo"

    def is_donator_only(self, image_type) -> bool:
        """
        Returns wether the image type requires a donator api key or not
        """
        return image_type in [
            ImageCategory.NSFW.COSPLAY,
            ImageCategory.NSFW.SWIMSUIT,
            ImageCategory.NSFW.PANTSU,
            ImageCategory.NSFW.NAKADASHI,
        ]
