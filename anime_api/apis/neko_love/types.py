from enum import Enum


class ImageCategory:
    """
    Image categories for the Neko-Love API
    """

    class SFW(Enum):
        """
        Safe For Work image types
        """

        NEKO = "neko"
        KITSUNE = "kitsune"
        HUG = "hug"
        PAT = "pat"
        WAIFU = "waifu"
        CRY = "cry"
        KISS = "kiss"
        SLAP = "slap"
        SMUG = "smug"
        PUNCH = "punch"

    class NSFW(Enum):
        """
        Not Safe For Work image types
        """

        NEKO = "nekolewd"
