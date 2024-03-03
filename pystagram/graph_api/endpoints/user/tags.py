from typing import List, Optional, Union

from pystagram.components.fields import MediaFields


class Tags:
    """ The `Tags` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `Tags` node of the Instagram Graph API."""
        self.user = user

    def get(self, user_id: Optional[str] = None, fields: Optional[List[Union[str, MediaFields]]] = None, access_token: Optional[str] = None):
        """ Get a collection of Instagram Media objects in which an Instagram User has been tagged by another Instagram user.
        :param user_id: The ID of the user to get tagged media from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param fields: A list of :class:`pystagram.graph_api.components.fields.media_fields.MediaFields` to get from the tagged media, defaults to None
        :type fields: Optional[List[Union[str, MediaFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/tags` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/tags", params=params)
