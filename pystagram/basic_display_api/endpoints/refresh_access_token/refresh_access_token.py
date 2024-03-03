from typing import Optional


class RefreshAccessToken:
    """ The `RefreshAccessToken` node of the Instagram Basic Display API.
    :param basic_display_api: An instance of the :class:`PystagramBasicDisplayApi` class.
    :type basic_display_api: :class:`PystagramBasicDisplayApi`
    """
    def __init__(self, basic_display_api: "PystagramBasicDisplayApi"):
        """ Initialize the `RefreshAccessToken` node of the Instagram Basic Display API."""
        self.basic_display_api = basic_display_api

    def get(self, access_token: str, grant_type: Optional[str] = "ig_exchange_token"):
        """ Gets a refreshed long-lived Instagram User Access Token that is at least 24 hours old but has not expired.
        :param access_token: The short-lived user access token, inferred from the `PystagramBasicDisplayApi` instance if None, defaults to None
        :type access_token: str, optional
        :param grant_type: The type of grant to request, defaults to "ig_exchange_token"
        :type grant_type: str, optional
        :return: The response from the `GET /access_token` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "grant_type": grant_type,
            "access_token": access_token or self.basic_display_api._access_token,
        }
        return self.basic_display_api.api_request(method="GET", endpoint="/refresh_access_token", params=params)
