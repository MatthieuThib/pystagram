from typing import Optional


class AccessToken:
    """ The `AccessToken` endpoint of the Instagram Graph API.
    :param oauth: An instance of the :class:`Oauth` class.
    :type oauth: :class:`Oauth`
    """
    def __init__(self, oauth: "Oauth"):
        """ Initializes the `AccessToken` class."""
        self.oauth = oauth

    def get(self, grant_type: Optional[str] = "fb_exchange_token", client_id: Optional[int] = None, client_secret: Optional[str] = None, fb_exchange_token: Optional[str] = None):
        """ Gets a Long-Lived User Access Token.
        Gets a long-lived user access token from a short-lived user access token.
        :param grant_type: The type of grant to request, defaults to "fb_exchange_token"
        :type grant_type: str, optional
        :param client_id: The app ID of the Instagram app, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type client_id: int, optional
        :param client_secret: The app secret of the Instagram app, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type client_secret: str, optional
        :param fb_exchange_token: The short-lived user access token, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type fb_exchange_token: str, optional
        :return: The response from the `GET /oauth/access_token` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "grant_type": grant_type,
            "client_id": client_id or self.oauth.graph_api.app_id,
            "client_secret": client_secret or self.oauth.graph_api.app_secret,
            "fb_exchange_token": fb_exchange_token or self.oauth.graph_api._access_token,
        }
        return self.oauth.graph_api.api_request(method="GET", endpoint="/oauth/access_token", params=params)
