from typing import Optional

from pystagram.helpers.errors import PystagramApiNotSupportedError


class Comments:
    """ The `Comments` node of the Instagram Graph API.
    :param media: An instance of the :class:`Media` class.
    :type media: :class:`Media`
    """
    def __init__(self, media: "Media"):
        """ Initialize the `Comments` node of the Instagram Graph API."""
        self.media = media

    def get(self, media_id: str, access_token: Optional[str] = None):
        """ Get comments on an Instagram media.
        :param media_id: The ID of the media to get comments from.
        :type media_id: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}/comments` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="GET", endpoint=f"/{media_id}/comments", params=params)

    def create(self, media_id: str, message: str, access_token: Optional[str] = None):
        """ Create a comment on an Instagram media.
        :param media_id: The ID of the media to create a comment on.
        :type media_id: str
        :param message: The message of the comment to create.
        :type message: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{media-id}/comments` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "message": message,
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="POST", endpoint=f"/{media_id}/comments", params=params)

    def update(self, *args, **kwargs):
        """ [Not Supported] Update a comment on an Instagram media.
        :raises InstagramApiNotSupportedError: Comment update is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Comment update is not supported by the Instagram Graph API.")

    def delete(self, *args, **kwargs):
        """ [Not Supported] Delete an Instagram comment on an Instagram media
        :raises InstagramApiNotSupportedError: Comment deletion is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Comment deletion is not supported by the Instagram Graph API.")
