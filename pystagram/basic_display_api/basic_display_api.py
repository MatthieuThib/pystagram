"""
**Instagram Basic Display API**
The Instagram Basic Display API allows users of your app to get basic profile information, photos, and videos
 in their Instagram accounts.The API can be used to access any type of Instagram account but only provides
 read-access to basic data. If you are building an app that will allow Instagram Businesses or Creators
 to publish media, moderate comments, identify @mentioned and hashtagged media, or get data about other
 Instagram users, use the Instagram Graph API instead.
"""
from typing import Optional

from pystagram.basic_display_api.endpoints import (
    AccessToken,
    Media,
    Oauth,
    RefreshAccessToken,
    User,
)
from pystagram.helpers.api_client import PystagramBaseApiClient


class PystagramBasicDisplayApi(PystagramBaseApiClient):

    BASE_URI: str = "graph.instagram.com"
    """ The base URI of the Instagram Basic Display API."""

    API_VERSION: str = "v18.0"
    """ The version of the Instagram Basic Display API."""

    ALTERNATE_URL: str = "api.instagram.com"
    """ An alternate base URI of the Instagram Basic Display API."""

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
        """ Initialize the Instagram Basic Display API client."""
        super().__init__(base_url=f"https://{base_uri}/{api_version}")
        self.app_id = app_id
        self.app_secret = app_secret
        self._access_token = access_token

    @property
    def access_token(self):
        """ The `AccessToken` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.media.media.Media` class for additional details.
        """
        return AccessToken(self)

    @property
    def media(self):
        """ The `Media` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.media.media.Media` class for additional details.
        """
        return Media(self)
    
    @property
    def oauth(self):
        """ The `OAuth` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.oauth.oauth.Oauth` class for additional details.
        """
        return Oauth(self)

    @property
    def user(self):
        """ The `User` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.user.user.User` class for additional details.
        """
        return User(self)

    @property
    def refresh_access_token(self):
        """ The `RefreshAccessToken` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.refresh_access_token.refresh_access_token.RefreshAccessToken` class for additional details.
        """
        return RefreshAccessToken(self)
