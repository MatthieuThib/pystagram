from typing import Optional

from pystagram.helpers.errors import (
    PystagramApiEndpointError,
    PystagramApiNotSupportedError,
)


class Stories:
    """ The `Stories` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `Stories` node of the Instagram Graph API."""
        self.user = user

    def get(self, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get a collection of story Instagram Media objects on an Instagram User.
        :param user_id: The ID of the user to get stories from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :return: The response from the `GET /{user-id}/stories` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/stories", params=params)

    def create(self, *args, **kwargs):
        """ [Not Supported] Create a story Instagram Media.
        :raises InstagramApiEndpointError: User story creation is supported by the User Media node
        """
        raise PystagramApiEndpointError(
            "User story creation is supported by the User Media node, "
            "consider using the User Media node to update a media."
            "See the :class:`pystagram.graph_api.endpoints.user.media.media.Media` class for additional details."
        )

    def update(self, *args, **kwargs):
        """ [Not Supported] Update a story Instagram Media.
        :raises InstagramApiNotSupportedError: Instagram user story update is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Story update is not supported by the Instagram Graph API")
    def delete(self, *args, **kwargs):
        """ [Not Supported] Delete a story Instagram Media.
        :raises InstagramApiNotSupportedError: Instagram user story deletion is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Story deletion is not supported by the Instagram Graph API")
