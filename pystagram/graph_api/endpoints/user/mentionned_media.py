from typing import List, Optional, Union

from pystagram.components.fields import MediaFields
from pystagram.helpers.decorators import cursor_paginated


class MentionedMedia:
    """ The `MentionedMedia` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `MentionedMedia` node of the Instagram Graph API."""
        self.user = user

    @cursor_paginated
    def get(self, media_id: int, fields: Optional[List[Union[str, MediaFields]]] = None, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get data on an Instagram Media in which an Instagram User has been @mentioned in a caption by another Instagram user. Paginated endpoint.
        :param media_id: The ID of the media to get data from.
        :type media_id: int
        :param fields: A list of :class:`pystagram.graph_api.components.fields.media_fields.MediaFields` to get from the media, defaults to None
        :type fields: Optional[List[Union[str, MediaFields]]], optional
        :param user_id: The ID of the user to get the mentioned media from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/mentioned_media` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        media_fields = fields if isinstance(fields, str) else ",".join(fields)
        fields = "mentioned_media.media_id({}){{{}}}".format(media_id, media_fields)
        return self.user.get(user_id=user_id, fields=fields, access_token=access_token)
