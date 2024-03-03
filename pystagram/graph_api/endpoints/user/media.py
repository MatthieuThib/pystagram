from typing import Optional, Type

from pystagram.components.containers.base_container import BaseContainer
from pystagram.helpers.decorators import cursor_paginated
from pystagram.helpers.errors import (
    PystagramApiEndpointError,
    PystagramApiNotSupportedError,
)


class Media:
    """ The `Media` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`    :param max_pages: The maximum number of pages to get from paginated endpoints, defaults to 5
    :type max_pages: int, optional
    """
    def __init__(self, user: "User"):
        """ Initialize the `Media` node of the Instagram Graph API."""
        self.user = user
        self.max_pages = self.user.graph_api.MAX_PAGES

    @cursor_paginated
    def get(self, user_id: Optional[str] = None, access_token: Optional[str] = None, limit: Optional[int] = 25, after: Optional[str] = None, before: Optional[str] = None):
        """ Get a collection of IG Media on an IG User. Paginated endpoint.
        :param user_id: The ID of the user to get media from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :param limit: The number of media to get per page, defaults to 25
        :type limit: int, optional
        :param after: The cursor to get the next page of media, defaults to None
        :type after: str, optional
        :param before: The cursor to get the previous page of media, defaults to None
        :type before: str, optional
        :return: The response from the `GET /{user-id}/media` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "limit": limit,
            "after": after,
            "before": before,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/media", params=params)

    def create(self, container: Type[BaseContainer], user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Create an image, carousel, story or reel Instagram Container.
        :param container: The container to create on the Instagram user. Can be an instance of the :class:`ImageContainer`, :class:`VideoContainer`, :class:`CarouselContainer`, :class:`StoryContainer` or :class:`ReelContainer` classes.
        :type container: Type[BaseContainer]
        :param user_id: The ID of the user to create the container on, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{user-id}/media` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            **container.fields,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="POST", endpoint=f"/{user_id}/media", params=params)

    def update(self, *args, **kwargs):
        """ [Not Supported] Update an Instagram Media.
        :raises InstagramApiEndpointError: User media update is only supported by the Media node
        """
        raise PystagramApiEndpointError(
            "User media update is only supported by the Media node, "
            "consider using the Media node to update a media."
            "See the :class:`pystagram.graph_api.endpoints.media.media.Media` class for additional details."
        )

    def delete(self):
        """ [Not Supported] Delete an Instagram Media.
        :raises InstagramApiNotSupportedError: Instagram user media deletion is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Media deletion is not supported by the Instagram Graph API")
