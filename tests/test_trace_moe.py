from anime_api.apis.trace_moe import TraceMoeAPI, File
from anime_api.apis.trace_moe.objects import Result


def test_search():
    """
    Test the search method. Should return a list of results.
    """
    image_url = "https://i.imgur.com/JAP73pV.jpg"
    results = TraceMoeAPI().search(File(url=image_url), True, True)

    assert isinstance(results, list)
    if len(results) > 0:
        for result in results:
            assert isinstance(result, Result), f"{result} is not a Result object"
