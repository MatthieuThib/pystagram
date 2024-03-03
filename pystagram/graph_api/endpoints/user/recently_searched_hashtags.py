from typing import Optional

from pystagram.helpers.decorators import cursor_paginated


class RecentlySearchedHashtags:
    """ The `RecentlySearchedHashtags` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `RecentlySearchedHashtags` node of the Instagram Graph API."""
        self.user = user

    @cursor_paginated
    def get(self, user_id: Optional[str] = None, limit: Optional[int] = None, access_token: Optional[str] = None):
        """ Get the hashtags that an Instagram User has queried using the Instagram Hashtags endpoint within the last 7 days.
        :param user_id: The ID of the user to get the recently searched hashtags from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param limit: The number of hashtags to get per page, defaults to None
        :type limit: int, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/recently_searched_hashtags` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "limit": limit,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/recently_searched_hashtags", params=params)
