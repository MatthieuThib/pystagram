from typing import Optional

from pystagram.helpers.decorators import alternate_url


class AccessToken:
    """ The `AccessToken` endpoint of the Instagram Basic Display API.
    :param oauth: An instance of the :class:`Oauth` class.
    :type oauth: :class:`Oauth`
    """
    def __init__(self, oauth: "Oauth"):
        """ Initializes the `AccessToken` class."""
        self.oauth = oauth

    @alternate_url
    def create(self, code: str, redirect_uri: str, client_id: Optional[int] = None, client_secret: Optional[str] = None, grant_type: Optional[str] = "authorization_code"):
        """ Gets a short-lived access token in exchange for an authorization code.
        :param code: The authorization code to exchange for a short-lived access token.
        :type code: str
        :param redirect_uri: The redirect URI used in the initial authorization request.
        :type redirect_uri: str
        :param client_id: The app ID of the Instagram app, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type client_id: int, optional
        :param client_secret: The app secret of the Instagram app, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type client_secret: str, optional
        :param grant_type: The type of grant to request, defaults to "authorization_code"
        :type grant_type: str, optional
        :return: The response from the `GET /oauth/access_token` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "client_id": client_id or self.oauth.basic_display.app_id,
            "client_secret": client_secret or self.oauth.basic_display.app_secret,
            "code": code,
            "grant_type": grant_type,
            "redirect_uri": redirect_uri
        }
        return self.oauth.basic_display.api_request(method="POST", endpoint="/oauth/access_token", params=params)
