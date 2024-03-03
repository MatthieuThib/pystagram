from typing import List, Optional, Union

from pystagram.components.fields import CommentFields
from pystagram.graph_api.endpoints.comment.replies import Replies
from pystagram.helpers.errors import PystagramApiNotSupportedError


class Comment:
    """ The `Comment` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `Comment` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, comment_id: str, fields: Optional[List[Union[str, CommentFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram comment.
        :param comment_id: The ID of the Instagram comment.
        :type comment_id: str
        :param fields: A list of :class:`pystagram.graph_api.components.fields.comment_fields.CommentFields` to get from the Comment node, defaults to None
        :type fields: Optional[List[Union[str, CommentFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{comment-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint=f"/{comment_id}", params=params)

    def create(self, *args, **kwargs):
        """ [Not Supported] Create an Instagram comment.
        :raises InstagramApiNotSupportedError: Comment creation is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Comment creation is not supported by the Instagram Graph API.")

    def update(self, comment_id: str, hide: Optional[bool] = False, access_token: Optional[str] = None):
        """ Update an Instagram comment.
        :param comment_id: The ID of the Instagram comment to update.
        :type comment_id: str
        :param hide: Whether to hide the comment, defaults to False
        :type hide: Optional[bool], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{comment-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "hide": hide,
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="POST", endpoint=f"/{comment_id}", params=params)

    def delete(self, comment_id: str, access_token: Optional[str] = None):
        """ Delete an Instagram comment.
        :param comment_id: The ID of the Instagram comment to delete.
        :type comment_id: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `DELETE /{comment-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="DELETE", endpoint=f"/{comment_id}", params=params)

    @property
    def replies(self):
        """ The `Replies` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.comment.replies.Replies` class for additional details.
        """
        return Replies(self)
