from typing import List, Optional, Union

from pystagram.components.scopes import Scopes
from pystagram.helpers.decorators import alternate_url


class Authorize:
    """ The `Authorize` endpoint of the Instagram Basic Display API.
    :param oauth: An instance of the :class:`Oauth` class.
    :type oauth: :class:`Oauth`
    """
    def __init__(self, oauth: "Oauth"):
        """ Initializes the `Authorize` class."""
        self.oauth = oauth

    @alternate_url
    def get(self, redirect_uri: str = None, scope: List[Union[str, Scopes]] = "user_profile", response_type: Optional[str] = "code", state: Optional[str] = None, client_id: Optional[int] = None):
        """ Gets the Authorization Window.
        Gets a long-lived user access token from a short-lived user access token.
        :param redirect_uri: The redirect URI used in the initial authorization request.
        :type redirect_uri: str
        :param scope: Permissions to request from the app user. user_profile is required.
        :type scope: List[Union[str, Scopes]], optional
        :param response_type: The type of response to request, defaults to "code"
        :type response_type: str, optional
        :param state: A server-specific state value to validate the request, defaults to None
        :param client_id: The app ID of the Instagram app, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type client_id: int, optional
        :return: The response from the `GET /oauth/access_token` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "redirect_uri": redirect_uri,
            "scope": scope if isinstance(scope, str) else ",".join(scope),
            "client_id": client_id or self.oauth.basic_display_api.app_id,
            "response_type": response_type,
            "state": state,
        }
        return self.oauth.basic_display_api.api_request(method="GET", endpoint="/oauth/authorize", params=params)
