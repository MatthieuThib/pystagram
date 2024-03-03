from typing import List, Optional, Union

from pystagram.components.fields import CommentFields
from pystagram.helpers.decorators import cursor_paginated


class MentionedComment:
    """ The `MentionedComment` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `MentionedComment` node of the Instagram Graph API."""
        self.user = user

    @cursor_paginated
    def get(self, comment_id: str, fields: Optional[List[Union[str, CommentFields]]] = None, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get data on an Instagram Comment in which an Instagram User has been @mentioned by another Instagram user. Paginated endpoint.
        :param comment_id: The ID of the comment to get data from.
        :type comment_id: str
        :param fields: A list of :class:`pystagram.graph_api.components.fields.comment_fields.CommentFields` to get from the comment, defaults to None
        :type fields: Optional[List[Union[str, CommentFields]]], optional
        :param user_id: The ID of the user to get the mentioned comment from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/mentioned_comment` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        comment_fields = fields if isinstance(fields, str) else ",".join(fields)
        fields = "mentioned_comment.comment_id({}){{{}}}".format(comment_id, comment_fields)
        return self.user.get(user_id=user_id, fields=fields, access_token=access_token)
