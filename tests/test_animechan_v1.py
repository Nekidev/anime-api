"""Offline contract tests; do not consume the provider's daily quota."""
from unittest.mock import Mock, patch

import pytest
import requests

from anime_api.apis import AnimechanV1API
from anime_api import exceptions


@pytest.mark.parametrize("filters,params", [
    ({}, {}),
    ({"anime_title": "Your Name & More"}, {"anime": "Your Name & More"}),
    ({"character_name": "Ran Mouri"}, {"character": "Ran Mouri"}),
])
def test_quote_contract(filters, params):
    response = Mock(status_code=200)
    response.json.return_value = {"status": "success", "data": {
        "content": "A quote", "anime": {"id": 1, "name": "An anime"},
        "character": {"id": 2, "name": "A character"},
    }}
    with patch("anime_api.apis.animechan_v1.requests.get", return_value=response) as get:
        quote = AnimechanV1API(endpoint="https://example.com/", timeout=3).get_random_quote(**filters)
    get.assert_called_once_with("https://example.com/quotes/random", params=params, timeout=3)
    assert (quote.anime, quote.character, quote.quote) == ("An anime", "A character", "A quote")


@pytest.mark.parametrize("status,error", [(404, exceptions.NotFound), (429, exceptions.ServerError), (500, exceptions.ServerError)])
def test_http_errors(status, error):
    with patch("anime_api.apis.animechan_v1.requests.get", return_value=Mock(status_code=status)):
        with pytest.raises(error):
            AnimechanV1API().get_random_quote()


def test_timeout_propagates_without_retry():
    with patch("anime_api.apis.animechan_v1.requests.get", side_effect=requests.Timeout) as get:
        with pytest.raises(requests.Timeout):
            AnimechanV1API().get_random_quote()
    assert get.call_count == 1


def test_conflicting_filters_do_not_send_request():
    with patch("anime_api.apis.animechan_v1.requests.get") as get:
        with pytest.raises(ValueError):
            AnimechanV1API().get_random_quote(anime_title="Anime", character_name="Character")
    get.assert_not_called()
