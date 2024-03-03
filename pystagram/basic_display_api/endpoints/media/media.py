from typing import List, Optional, Union

from pystagram.basic_display_api.endpoints.media.children import Children
from pystagram.components.fields import MediaFields


class Media:
    """ The `Media` node of the Instagram Basic Display API.
    :param basic_display_api: An instance of the :class:`InstagramBasicDisplayApi` class.
    :type basic_display_api: :class:`InstagramBasicDisplayApi`
    """
    def __init__(self, basic_display_api: "PystagramBasicDisplayApi"):
        """ Initialize the `Media` node of the Instagram Basic Display API."""
        self.basic_display_api = basic_display_api

    def get(self, media_id: str, fields: Optional[List[Union[str, MediaFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram media.
        :param media_id: The ID of the media to get fields and edges from.
        :type media_id: str
        :param fields: A list of :class:`pystagram.basic_display_api.components.fields.media_fields.MediaFields` to get from the media, defaults to None
        :type fields: Optional[List[Union[str, MediaFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramBasicDisplayApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.basic_display_api._access_token,
        }
        return self.basic_display_api.api_request(method="GET", endpoint=f"/{media_id}", params=params)

    @property
    def children(self):
        """ The ``Children` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.media.children.Children` class for more information.
        """
        return Children(self)
