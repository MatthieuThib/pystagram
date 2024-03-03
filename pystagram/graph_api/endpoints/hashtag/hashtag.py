from typing import List, Optional, Union

from pystagram.components.fields import HashtagFields
from pystagram.graph_api.endpoints.hashtag.recent_media import RecentMedia
from pystagram.graph_api.endpoints.hashtag.top_media import TopMedia


class Hashtag:
    """ The `Hashtag` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `Hashtag` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, hashtag_id: str, fields: Optional[List[Union[str, HashtagFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram hashtag.
        :param hashtag_id: The ID of the hashtag to get fields and edges from.
        :type hashtag_id: str
        :param fields: A list of :class:`pystagram.graph_api.components.fields.hashtag_fields.HashtagFields` to get from the hashtag, defaults to None
        :type fields: Optional[List[Union[str, HashtagFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{hashtag-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint=f"/{hashtag_id}", params=params)

    @property
    def recent_media(self):
        """ The `RecentMedia` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.hashtag.recent_media.RecentMedia` class for more information.
        """
        return RecentMedia(self)

    @property
    def top_media(self):
        """ The `TopMedia` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.hashtag.top_media.TopMedia` class for more information.
        """
        return TopMedia(self)
