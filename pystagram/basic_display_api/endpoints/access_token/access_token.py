from typing import Optional


class AccessToken:
    """ The `AccessToken` node of the Instagram Basic Display API.
    :param basic_display_api: An instance of the :class:`PystagramGraphApi` class.
    :type basic_display_api: :class:`PystagramGraphApi`
    """
    def __init__(self, basic_display_api: "PystagramBasicDisplayApi"):
        """ Initialize the `AccessToken` node of the Instagram Basic Display API."""
        self.basic_display_api = basic_display_api

    def get(self, grant_type: Optional[str] = "ig_exchange_token", client_id: Optional[int] = None, client_secret: Optional[str] = None, access_token: Optional[str] = None):
        """ Gets a Long-Lived User Access Token.
        Gets a long-lived user access token from a short-lived user access token.
        :param grant_type: The type of grant to request, defaults to "ig_exchange_token"
        :type grant_type: str, optional
        :param client_id: The app ID of the Instagram app, inferred from the `PystagramBasicDisplayApi` instance if None, defaults to None
        :type client_id: int, optional
        :param client_secret: The app secret of the Instagram app, inferred from the `PystagramBasicDisplayApi` instance if None, defaults to None
        :type client_secret: str, optional
        :param access_token: The short-lived user access token, inferred from the `PystagramBasicDisplayApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /access_token` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "grant_type": grant_type,
            "client_id": client_id or self.basic_display_api.app_id,
            "client_secret": client_secret or self.basic_display_api.app_secret,
            "access_token": access_token or self.basic_display_api._access_token,
        }
        return self.basic_display_api.api_request(method="GET", endpoint="/access_token", params=params)
