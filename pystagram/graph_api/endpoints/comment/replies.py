from typing import Optional

from pystagram.helpers.errors import PystagramApiNotSupportedError


class Replies:
    """ The `Replies` node of the Instagram Graph API.
    :param comment: An instance of the :class:`Comment` class.
    :type comment: :class:`Comment`
    """
    def __init__(self, comment: "Comment"):
        """ Initialize the `Replies` node of the Instagram Graph API."""
        self.comment = comment

    def get(self, comment_id: str, access_token: Optional[str] = None):
        """ Get all replies on an Instagram comment.
        :param comment_id: The ID of the Instagram comment.
        :type comment_id: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{comment-id}/replies` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "access_token": access_token or self.comment.graph_api._access_token,
        }
        return self.comment.graph_api.api_request(method="GET", endpoint=f"/{comment_id}/replies", params=params)

    def create(self, comment_id: str, message: str, access_token: Optional[str] = None):
        """ Create a reply to an Instagram comment.
        :param comment_id: The ID of the Instagram comment.
        :type comment_id: str
        :param message: The message of the reply.
        :type message: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{comment-id}/replies` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "message": message,
            "access_token": access_token or self.comment.graph_api._access_token,
        }
        return self.comment.graph_api.api_request(method="POST", endpoint=f"/{comment_id}/replies", params=params)

    def update(self, *args, **kwargs):
        """ [Not Supported] Update an Instagram comment reply.
        :raises InstagramApiNotSupportedError: Comment reply update is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Comment reply update is not supported by the Instagram Graph API.")

    def delete(self, *args, **kwargs):
        """ [Not Supported] Delete an Instagram comment reply.
        :raises InstagramApiNotSupportedError: Comment reply deletion is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Comment reply deletion is not supported by the Instagram Graph API.")
