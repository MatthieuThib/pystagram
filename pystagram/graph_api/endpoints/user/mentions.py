from typing import Optional


class Mentions:
    """ The `Mentions` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `Mentions` node of the Instagram Graph API."""
        self.user = user

    def create(self, media_id: str, message: str, comment_id: Optional[str] = None, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Creates an Instagram Comment on an Instagram Media or Instagram comment in which an Instagram User has been @mentioned in.
        :param media_id: The ID of the media where the user was mentioned.
        :type media_id: str
        :param message: The comment message.
        :type message: str
        :param user_id: The ID of the user to mention, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{user-id}/mentions` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "media_id": media_id,
            "comment_id": comment_id,
            "message": message,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="POST", endpoint=f"/{user_id}/mentions", params=params)
