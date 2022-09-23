from enum import Enum

import random


class ImageCategory:
    """
    Image's category
    """

    class SFW(Enum):
        """
        Safe For Work endpoints
        """

        WAVE = "wave"
        WINK = "wink"
        TEA = "tea"
        BONK = "bonk"
        PUNCH = "punch"
        POKE = "poke"
        BULLY = "bully"
        PAT = "pat"
        KISS = "kiss"
        KICK = "kick"
        BLUSH = "blush"
        FEED = "feed"
        SMUG = "smug"
        HUG = "hug"
        CUDDLE = "cuddle"
        CRY = "cry"
        CRINGE = "cringe"
        SLAP = "slap"
        FIVE = "five"
        GLOMP = "glomp"
        HAPPY = "happy"
        HOLD = "hold"
        NOM = "nom"
        SMILE = "smile"
        THROW = "throw"
        LICK = "lick"
        BITE = "bite"
        DANCE = "dance"
        BOOP = "boop"
        SLEEP = "sleep"
        LIKE = "like"
        KILL = "kill"
        TICKLE = "tickle"
        NOSEBLEED = "nosebleed"
        THREATEN = "threaten"
        DEPRESSION = "depression"
        WOLF = "wolf_arts"
        JAHY = "jahy_arts"
        NEKO = "neko_arts"
        COFFEE_ARTS = "coffee_arts"
        WALLPAPER = "wallpaper"
        MOBILE_WALLPAPER = "mobileWallpaper"

        @property
        def RANDOM(self):
            """
            Returns a random SFW image type
            """
            return ImageCategory.SFW(random.choice(list(self)))

    class NSFW(Enum):
        """
        Not Safe For Work endpoints
        """

        ASS = "ass"
        ANAL = "anal"
        BDSM = "bdsm"
        CLASSIC = "classic"
        CUM = "cum"
        CREAMPIE = "creampie"
        MANGA = "manga"
        FEMDOM = "femdom"
        HENTAI = "hentai"
        INCEST = "incest"
        MASTURBATION = "masturbation"
        PUBLIC = "public"
        ERO = "ero"
        ORGY = "orgy"
        ELVES = "elves"
        YURI = "yuri"
        PANTSU = "pantsu"
        PUSSY = "pussy"
        GLASSES = "glasses"
        CUCKOLD = "cuckold"
        BLOWJOB = "blowjob"
        BOOBJOB = "boobjob"
        HANDJOB = "handjob"
        FOOTJOB = "footjob"
        BOOBS = "boobs"
        THIGHS = "thighs"
        AHEGAO = "ahegao"
        UNIFORM = "uniform"
        GANGBANG = "gangbang"
        TENTACLES = "tentacles"
        GIF = "gif"
        NEKO = "nsfwNeko"
        MOBILE_WALLPAPER = "nsfwMobileWallpaper"
        ZETTAI_RYOUIKI = "zettaiRyouiki"

        @property
        def RANDOM(self):
            """
            Returns a random NSFW image type
            """
            return ImageCategory.NSFW(random.choice(list(self)))
