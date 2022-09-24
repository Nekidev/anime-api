from enum import Enum


class SearchSort(Enum):
    """
    Sort order for search results.
    """

    NEWEST = "newest"
    OLDEST = "oldest"
    RELEVANCE = "relevance"
    LIKES = "likes"
