"""
Run tests for the NekosAPI class

Usage:
    cd tests
    poetry run python -m pytest nekos_api.py
"""
from anime_api.apis import NekosAPI
from anime_api.apis.nekos_api.objects import Image, Category, Character, Artist


# If you have an access token, replace it here to test endpoints that require
# authentication.
TOKEN = "a" * 100

api = NekosAPI(token=TOKEN)


def check_image(image):
    assert isinstance(image, Image), "Returned obeject is not an image"
    for category in image.categories:
        assert isinstance(
            category, Category
        ), "Image categories are not category objects"
    for character in image.characters:
        assert isinstance(
            character, Character
        ), "Image characters are not character objects"
    assert "kemonomimi" in [
        c.name.lower() for c in image.categories
    ], "Selected category is not in image categories"
    assert isinstance(image.artist, Artist) | isinstance(
        image.artist, type(None)
    ), "Artist is not an artist object"


def test_get_images():
    """
    Tests the get_images method. This will fail if you do not have an access
    token.
    """
    images = api.get_images(limit=10, offset=0)
    assert len(images) == 10, "There are not as many images as specified"
    for image in images:
        check_image(image)


def test_get_random_image():
    """
    Tests the get_random_image method
    """
    image = api.get_random_image(categories=["kemonomimi"])
    check_image(image)


def test_get_random_images():
    """
    Tests the get_random_images method
    """
    images = api.get_random_images(10, categories=["kemonomimi"])
    assert len(images) == 10, "There are not as many images as specified"
    for image in images:
        check_image(image)


def test_get_image_by_id():
    """
    Tests the get_image_by_id method
    """
    image = api.get_image_by_id(image_id="e80cc896-a51e-4b71-bbad-e4137e15c30d")
    check_image(image)


def test_get_artists():
    """
    Tests the get_artists method
    """
    artists = api.get_artists(limit=10, offset=0)
    for artist in artists:
        assert isinstance(artist, Artist), "Result contains non Artist object items"


def test_get_artist_by_id():
    """
    Tests the get_artist_by_id method
    """
    artist = api.get_artist_by_id(artist_id="ea6e23ab-d0fc-4ede-984a-350a07e41ced")
    assert isinstance(artist, Artist)


def test_get_images_by_artist_id():
    """
    Tests the get_images_by_artist_id method
    """
    images = api.get_images_by_artist_id(
        artist_id="ea6e23ab-d0fc-4ede-984a-350a07e41ced", limit=10, offset=0
    )
    assert isinstance(images, list), "Result is not a list"
    for image in images:
        assert isinstance(image, Image), "Result contains non-Image items"


def test_get_categories():
    """
    Tests the get_categories method
    """
    categories = api.get_categories(limit=10, offset=0)
    assert isinstance(categories, list), "Result is not a list"
    assert (
        len(categories) == 10
    ), "Result does not contain the requested amount of categories"
    for category in categories:
        assert isinstance(category, Category), "Result contains non-category items"


def test_get_category_by_id():
    """
    Tests the get_category_by_id method
    """
    category = api.get_category_by_id(
        category_id="05140510-d7e8-43bc-a66f-7afaf1fcdf29"
    )
    assert isinstance(category, Category)


def test_get_character_by_id():
    """
    Tests the get_character_by_id method
    """
    character = api.get_character_by_id(
        character_id="25af3b5c-4671-4017-8794-e5caf7078e59"
    )
    assert isinstance(character, Character), "Result is not a Character object"
