from typing import Optional


class Children:
    """ The `Children` node of the Instagram Basic Display API.
    :param media: An instance of the :class:`Media` class.
    :type media: :class:`Media`
    """
    def __init__(self, media: "Media"):
        """ Initialize the `Children` node of the Instagram Basic Display API."""
        self.media = media

    def get(self, media_id: str, access_token: Optional[str] = None):
        """ Get a list of Instagram Media objects on an Instagram album Media object.
        :param media_id: The ID of the media to get children from.
        :type media_id: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}/children` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "access_token": access_token or self.media.basic_display_api._access_token,
        }
        return self.media.basic_display_api.api_request(method="GET", endpoint=f"/{media_id}/children", params=params)
