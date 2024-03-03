"""
**Instagram Graph API**
The `Instagram Graph API <https://developers.facebook.com/docs/instagram-api>`_ allows users of your app to access data
in their `Instagram Business <https://business.instagram.com/>`_ and `Instagram Creator <https://help.instagram.com/2358103564437429>`_ accounts.
The API can be used to get and publish their media, manage and reply to comments on their media,
identify media where they have been @mentioned by components Instagram users, find hashtagged media,
and get basic metadata and metrics about components Instagram Businesses and Creators.
"""

from typing import Optional

from pystagram.components.fields import AccountFields
from pystagram.graph_api.endpoints import (
    Comment,
    Container,
    Hashtag,
    HashtagSearch,
    Me,
    Media,
    Oauth,
    User,
)
from pystagram.helpers.api_client import PystagramBaseApiClient


class PystagramGraphApi(PystagramBaseApiClient):
    """ Client for making requests to the Instagram Graph API.
    It extends the :class:`pystagram.helpers.api_client.base_api_client.InstagramBaseApiClient` class.
    :param app_id: The app ID of the Instagram app.
    :type app_id: int    :param app_secret: The app secret of the Instagram app.
    :type app_secret: str    :param access_token: The access token of the Instagram app, defaults to None
    :type access_token: str, optional    :param base_uri: The base URL of the Instagram Graph API, defaults to BASE_URI
    :type base_uri: str, optional    :param api_version: The version of the Instagram Graph API, defaults to API_VERSION
    :type api_version: str, optional
    """

    BASE_URI: str = "graph.facebook.com"
    """ The base URI of the Instagram Graph API."""
    API_VERSION: str = "v18.0"
    """ The version of the Instagram Graph API."""

    MAX_PAGES: int = None
    """ The maximum number of pages to get from paginated endpoints, defaults to None (no limit)."""

    def __init__(
        self,
        app_id: int,
        app_secret: str,
        access_token: Optional[str] = None,
        base_uri: Optional[str] = BASE_URI,
        api_version: Optional[str] = API_VERSION,
    ):
        """ Initialize the Instagram Graph API client."""
        super().__init__(base_url=f"https://{base_uri}/{api_version}")
        self.app_id = app_id
        self.app_secret = app_secret
        self._access_token = access_token
        self._user_id = None

    def get_user_id(self):
        """ Get the user ID of the Instagram user.

        :return: The user ID of the Instagram user.
        :rtype: str
        """
        return (
            self.me.accounts.get(
                fields=[AccountFields.INSTAGRAM_BUSINESS_ACCOUNT],
                access_token=self._access_token,
            )
            .data.get("data", list(dict()))[0]
            .get(AccountFields.INSTAGRAM_BUSINESS_ACCOUNT, dict())
            .get(AccountFields.ID, 0)
        )

    @property
    def user_id(self):
        """ The user ID of the Instagram user.
        The user id is fetched from the Instagram Graph API if it is not already set.
        """
        return self._user_id or self.get_user_id()

    @property
    def oauth(self):
        """ The `OAuth` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.oauth.oauth.Oauth` class for additional details.
        """
        return Oauth(self)

    @property
    def me(self):
        """ The `Me` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.me.me.Me` class for additional details.
        """
        return Me(self)

    @property
    def comment(self):
        """ The `Comment` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.comment.comment.Comment` class for additional details.
        """
        return Comment(self)

    @property
    def container(self):
        """ The `Container` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.container.container.Container` class for additional details.
        """
        return Container(self)

    @property
    def hashtag_search(self):
        """ The `HashtagSearch` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.hashtag_search.HashtagSearch` class for additional details.
        """
        return HashtagSearch(self)

    @property
    def hashtag(self):
        """ The `Hashtag` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.hashtag.hashtag.Hashtag` class for additional details.
        """
        return Hashtag(self)

    @property
    def media(self):
        """ The `Media` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.media.media.Media` class for additional details.
        """
        return Media(self)

    @property
    def user(self):
        """ The `User` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.user.User` class for additional details.
        """
        return User(self)
