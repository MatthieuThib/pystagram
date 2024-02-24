from typing import Optional


class MediaPublish:
    """ The `MediaPublish` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `MediaPublish` node of the Instagram Graph API."""
        self.user = user

    def create(self, container_id: str, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Publish an Instagram Media Container.
        :param container_id: The ID of the container to publish on the Instagram user.
        :type container_id: str
        :param user_id: The ID of the user to publish the container on, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{user-id}/media_publish` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "creation_id": container_id,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="POST", endpoint=f"/{user_id}/media_publish", params=params)
