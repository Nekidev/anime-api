"""
Module for waifu.im API types.
"""

import enum


class ImageTag:
    """
    Image type.
    """

    class SFW(enum.Enum):
        """
        Safe For Work image types.
        """

        MAID = "maid"
        WAIFU = "waifu"
        MARIN_KITAGAWA = "marin-kitagawa"
        MORI_CALLIOPE = "mori-calliope"
        RAIDEN_SHOGUN = "raiden-shogun"
        OPPAI = "oppai"
        SELFIES = "selfies"
        UNIFORM = "uniform"

    class NSFW(enum.Enum):
        """
        Not Safe For Work image types.
        """

        ASS = "ass"
        HENTAI = "hentai"
        MILF = "milf"
        ORAL = "oral"
        PAIZURI = "paizuri"
        ECCHI = "ecchi"
        ERO = "ero"

    def get_tag(self, value: str):
        """
        Get ImageTag from string value
        """
        try:
            return ImageTag.SFW(value)
        except ValueError:
            return ImageTag.NSFW(value)


class SearchSort(enum.Enum):
    """
    Sort order for search results.
    """

    FAVORITES = "FAVOURITES"
    UPLOADED_AT = "UPLOADED_AT"
    RANDOM = "RANDOM"


class ImageOrientation(enum.Enum):
    """
    Image orientation
    """

    HORIZONTAL = "landscape"
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"
    VERTICAL = "portrait"
