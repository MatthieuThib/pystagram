from typing import Optional

from pystagram.helpers.decorators import cursor_paginated


class UserMedia:
    """ The `UserMedia` node of the Instagram Basic Display API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    :param max_pages: The maximum number of pages to get from paginated endpoints, defaults to 5
    :type max_pages: int, optional
    """
    def __init__(self, user: "User"):
        """ Initialize the `UserMedia` node of the Instagram Basic Display API."""
        self.user = user
        self.max_pages = self.user.basic_display_api.MAX_PAGES

    @cursor_paginated
    def get(self, user_id: Optional[str] = None, access_token: Optional[str] = None, limit: Optional[int] = 25, after: Optional[str] = None, before: Optional[str] = None):
        """ Get a collection of IG Media on an IG User. Paginated endpoint.
        :param user_id: The ID of the user to get media from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :param limit: The number of media to get per page, defaults to 25
        :type limit: int, optional
        :param after: The cursor to get the next page of media, defaults to None
        :type after: str, optional
        :param before: The cursor to get the previous page of media, defaults to None
        :type before: str, optional
        :return: The response from the `GET /{user-id}/media` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.basic_display_api.user_id
        params = {
            "limit": limit,
            "after": after,
            "before": before,
            "access_token": access_token or self.user.basic_display_api._access_token,
        }
        return self.user.basic_display_api.api_request(method="GET", endpoint=f"/{user_id}/media", params=params)
