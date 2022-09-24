from dataclasses import dataclass

import datetime
import typing


@dataclass
class User:
    """
    Object representation of an user
    """

    _api: object

    _id: str
    _username: typing.Optional[str] = None
    _created_at: typing.Optional[datetime.datetime] = None
    _favorites: typing.Optional[typing.List['Image']] = None
    _favorites_received: typing.Optional[int] = None
    _likes: typing.Optional[typing.List['Image']] = None
    _likes_received: typing.Optional[int] = None
    _roles: typing.Optional[typing.List[str]] = None
    _saved_tags: typing.Optional[typing.List[str]] = None
    _uploads: typing.Optional[typing.List[str]] = None

    def load(self):
        """
        Load the user object
        """

        user_info: User = self._api.get_user(self._id)

        self._username = user_info._username
        self._created_at = user_info._created_at
        self._favorites = user_info._favorites
        self._favorites_received = user_info._favorites_received
        self._likes = user_info._likes
        self._likes_received = user_info._likes_received
        self._roles = user_info._roles
        self._saved_tags = user_info._saved_tags
        self._uploads = user_info._uploads

    @property
    def is_loaded(self):
        """
        Check if the user object is loaded
        """

        return self._username is not None and self._created_at is not None

    @property
    def id(self) -> str:
        """
        Get the user ID
        """

        if not self.is_loaded and not self._id:
            self.load()

        return self._id

    @property
    def username(self) -> str:
        """
        Get the user username
        """

        if not self.is_loaded:
            self.load()

        return self._username

    @property
    def created_at(self) -> datetime.datetime:
        """
        Get the user creation date
        """

        if not self.is_loaded and not self._created_at:
            self.load()

        return self._created_at

    @property
    def favorites(self) -> typing.List[str]:
        """
        Get the user favorites
        """

        if not self.is_loaded and not self._favorites:
            self.load()

        return self._favorites

    @property
    def favorites_received(self) -> int:
        """
        Get the user favorites received
        """

        if not self.is_loaded and not self._favorites_received:
            self.load()

        return self._favorites_received

    @property
    def likes(self) -> typing.List[str]:
        """
        Get the user likes
        """

        if not self.is_loaded and not self._likes:
            self.load()

        return self._likes

    @property
    def likes_received(self) -> int:
        """
        Get the user likes received
        """

        if not self.is_loaded and not self._likes_received:
            self.load()

        return self._likes_received

    @property
    def roles(self) -> typing.List[str]:
        """
        Get the user roles
        """

        if not self.is_loaded and not self._roles:
            self.load()

        return self._roles

    @property
    def saved_tags(self) -> typing.List[str]:
        """
        Get the user saved tags
        """

        if not self.is_loaded and not self._saved_tags:
            self.load()

        return self._saved_tags

    @property
    def uploads(self) -> typing.List[str]:
        """
        Get the user uploads
        """

        if not self.is_loaded and not self._uploads:
            self.load()

        return self._uploads


@dataclass
class Image:
    """
    Object representation of an image
    """

    _api: object

    _id: str
    _nsfw: typing.Optional[bool] = None
    _tags: typing.Optional[typing.List[str]] = None
    _likes: typing.Optional[int] = None
    _favorites: typing.Optional[int] = None
    _uploader: typing.Optional[User] = None
    _approver: typing.Optional[User] = None
    _artist: typing.Optional[str] = None
    _created_at: typing.Optional[datetime.datetime] = None
    _pending: typing.Optional[bool] = None

    def load(self):
        """
        Load the image object
        """

        image_info: Image = self._api.get_image(self._id)

        self._nsfw = image_info._nsfw
        self._tags = image_info._tags
        self._likes = image_info._likes
        self._favorites = image_info._favorites
        self._uploader = image_info._uploader
        self._approver = image_info._approver
        self._artist = image_info._artist
        self._created_at = image_info._created_at
        self._pending = image_info._pending

    @property
    def is_loaded(self):
        """
        Check if the image object is loaded
        """

        return self._uploader is not None and self._created_at is not None

    @property
    def id(self) -> str:
        """
        Get the image ID
        """

        if not self.is_loaded and not self._id:
            self.load()

        return self._id

    @property
    def nsfw(self) -> bool:
        """
        Check if the image is NSFW
        """

        if not self.is_loaded and self._nsfw is None:
            self.load()

        return self._nsfw

    @property
    def tags(self) -> typing.List[str]:
        """
        Get the image tags
        """

        if not self.is_loaded and not self._tags:
            self.load()

        return self._tags

    @property
    def likes(self) -> int:
        """
        Get the image likes
        """

        if not self.is_loaded and not self._likes:
            self.load()

        return self._likes

    @property
    def favorites(self) -> int:
        """
        Get the image favorites
        """

        if not self.is_loaded and not self._favorites:
            self.load()

        return self._favorites

    @property
    def uploader(self) -> User:
        """
        Get the image uploader
        """

        if not self.is_loaded and not self._uploader:
            self.load()

        return self._uploader

    @property
    def approver(self) -> User:
        """
        Get the image approver
        """

        if not self.is_loaded and not self._approver:
            self.load()

        return self._approver

    @property
    def artist(self) -> str:
        """
        Get the image artist
        """

        if not self.is_loaded and not self._artist:
            self.load()

        return self._artist

    @property
    def created_at(self) -> datetime.datetime:
        """
        Get the image creation date
        """

        if not self.is_loaded and not self._created_at:
            self.load()

        return self._created_at

    @property
    def url(self):
        """
        Get the image URL
        """

        return f"https://nekos.moe/image/{self.id}"

    @property
    def pending(self) -> bool:
        """
        Check if the image is pending
        """

        if not self.is_loaded and self._pending is None:
            self.load()

        return self._pending


@dataclass
class PendingImage:
    """
    Object representation of an image that is being uploaded
    """

    image: Image
    image_url: str
    post_url: str
