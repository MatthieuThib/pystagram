from typing import List, Optional, Union

from pystagram.components.fields import MediaFields


class RecentMedia:
    """ The `RecentMedia` node of the Instagram Graph API.
    :param hashtag: An instance of the :class:`Hashtag` class.
    :type hashtag: :class:`Hashtag`
    """
    def __init__(self, hashtag: "Hashtag"):
        """ Initialize the `RecentMedia` node of the Instagram Graph API."""
        self.hashtag = hashtag

    def get(self, hashtag_id: str, user_id: Optional[str] = None, fields: Optional[List[Union[str, MediaFields]]] = None, access_token: Optional[str] = None):
        """ Get a list of the most recently published photo and video Instagram Media objects published with a specific hashtag.
        :param hashtag_id: The ID of the hashtag to get recent media from.
        :type hashtag_id: str
        :param user_id: The ID of the Instagram user performing the query, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param fields: A list of :class:`pystagram.graph_api.components.fields.media_fields.MediaFields` to get from the recent media, defaults to None
        :type fields: Optional[List[Union[str, MediaFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{hashtag-id}/recent_media` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "user_id": user_id or self.hashtag.graph_api.user_id,
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.hashtag.graph_api._access_token,
        }
        return self.hashtag.graph_api.api_request(method="GET", endpoint=f"/{hashtag_id}/recent_media", params=params)
