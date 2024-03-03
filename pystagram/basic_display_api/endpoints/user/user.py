from typing import List, Optional, Union

from pystagram.basic_display_api.endpoints.user.user_media import UserMedia
from pystagram.components.fields import UserFields


class User:
    """ The `User` node of the Instagram Basic Display API.
    :param basic_display_api: An instance of the :class:`PystagramGraphApi` class.
    :type basic_display_api: :class:`PystagramGraphApi`
    """
    def __init__(self, basic_display_api: "PystagramBasicDisplayApi"):
        """ Initialize the `User` node of the Instagram Basic Display API."""
        self.basic_display_api = basic_display_api

    def get(self, user_id: Optional[str] = "me", fields: Optional[List[Union[str, UserFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram Business or Creator Account.
        :param user_id: The ID of the user to get fields and edges from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param fields: A list of :class:`pystagram.basic_display_api.components.fields.user_fields.UserFields` to get from the user, defaults to None
        :type fields: Optional[List[Union[str, UserFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.basic_display_api.user_id
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.basic_display_api._access_token,
        }
        return self.basic_display_api.api_request(method="GET", endpoint=f"/{user_id}", params=params)

    @property
    def user_media(self):
        """ The `Media` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.user.media.Media` class for additional details.
        """
        return UserMedia(self)
