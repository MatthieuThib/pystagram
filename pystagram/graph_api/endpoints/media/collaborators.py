from typing import Optional


class Collaborators:
    """ The `Collaborators` node of the Instagram Graph API.
    :param media: An instance of the :class:`Media` class.
    :type media: :class:`Media`
    """
    def __init__(self, media: "Media"):
        """ Initialize the `Collaborators` node of the Instagram Graph API."""
        self.media = media

    def get(self, media_id: str, access_token: Optional[str] = None):
        """ Get a list of Instagram users as collaborators and their invitation status on an IG Media object.
        :param media_id: The ID of the media to get collaborators from.
        :type media_id: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}/collaborators` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="GET", endpoint=f"/{media_id}/collaborators", params=params)
