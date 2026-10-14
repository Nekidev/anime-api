"""Network-free link-audit classification tests."""
import urllib.error
from unittest.mock import Mock, patch

import pytest

from scripts.check_links import check_url


@pytest.mark.parametrize("status,state", [(404, "missing"), (410, "missing"), (403, "unverified"), (429, "unverified"), (503, "unverified")])
def test_http_classification(status, state):
    error = urllib.error.HTTPError("https://example.com", status, "test", {}, None)
    with patch("urllib.request.urlopen", side_effect=error):
        assert check_url("https://example.com")["state"] == state


def test_transport_failure_is_not_removal_evidence():
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("DNS failed")):
        assert check_url("https://example.com")["state"] == "unverified"


@pytest.mark.parametrize("body,state", [(b"API docs", "reachable"), (b'window.location.href="/lander"', "parked")])
def test_success_and_parking(body, state):
    response = Mock(status=200, url="https://example.com/docs")
    response.read.return_value = body
    context = Mock()
    context.__enter__ = Mock(return_value=response)
    context.__exit__ = Mock(return_value=False)
    with patch("urllib.request.urlopen", return_value=context):
        result = check_url("https://example.com/docs")
    assert result["state"] == state
    assert result["status"] == 200
