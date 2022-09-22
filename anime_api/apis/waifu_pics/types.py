"""
Module for Waifu Pics API types.
"""
from enum import Enum


class ImageCategory:
    """
    Image category.
    """

    class SFW(Enum):
        """
        Safe for work image type.
        """

        WAIFU = "waifu"
        NEKO = "neko"
        SHINOBU = "shinobu"
        MEGUMIN = "megumin"
        BULLY = "bully"
        CUDDLE = "cuddle"
        CRY = "cry"
        HUG = "hug"
        AWOO = "awoo"
        KISS = "kiss"
        LICK = "lick"
        PAT = "pat"
        SMUG = "smug"
        BONK = "bonk"
        YEET = "yeet"
        BLUSH = "blush"
        SMILE = "smile"
        WAVE = "wave"
        HIGHFIVE = "highfive"
        HANDHOLD = "handhold"
        NOM = "nom"
        BITE = "bite"
        GLOMP = "glomp"
        SLAP = "slap"
        KILL = "kill"
        KICK = "kick"
        HAPPY = "happy"
        WINK = "wink"
        POKE = "poke"
        DANCE = "dance"
        CRINGE = "cringe"

    class NSFW(Enum):
        """
        Not safe for work image type.
        """

        WAIFU = "waifu"
        NEKO = "neko"
        TRAP = "trap"
        BLOWJOB = "blowjob"
