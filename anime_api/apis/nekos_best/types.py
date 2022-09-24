from enum import Enum


class ImageCategory(Enum):
    """
    Image's category
    """

    HIGHFIVE = "highfive"
    HAPPY = "happy"
    SLEEP = "sleep"
    HANDHOLD = "handhold"
    LAUGH = "laugh"
    BITE = "bite"
    POKE = "poke"
    TICKLE = "tickle"
    KISS = "kiss"
    WAVE = "wave"
    THUMBSUP = "thumbsup"
    STARE = "stare"
    CUDDLE = "cuddle"
    SMILE = "smile"
    BAKA = "baka"
    BLUSH = "blush"
    THINK = "think"
    POUT = "pout"
    FACEPALM = "facepalm"
    WINK = "wink"
    SHOOT = "shoot"
    SMUG = "smug"
    CRY = "cry"
    PAT = "pat"
    PUNCH = "punch"
    DANCE = "dance"
    FEED = "feed"
    SHRUG = "shrug"
    BORED = "bored"
    KICK = "kick"
    HUG = "hug"
    YEET = "yeet"
    SLAP = "slap"
    NEKO = "neko"
    HUSBANDO = "husbando"
    KITSUNE = "kitsune"
    WAIFU = "waifu"


class ImageType(Enum):
    """
    Image format
    """

    IMAGE = 1
    GIF = 2
