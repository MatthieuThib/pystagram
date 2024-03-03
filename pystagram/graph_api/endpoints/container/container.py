from typing import List, Optional, Union

from pystagram.components.fields import ContainerFields
from pystagram.helpers.errors import (
    PystagramApiEndpointError,
    PystagramApiNotSupportedError,
)


class Container:
    """ The `Container` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """

    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `Container` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, container_id: int, fields: Optional[List[Union[str, ContainerFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram container.
        :param container_id: The ID of the container to get fields and edges from.
        :type container_id: int
        :param fields: A list of :class:`pystagram.graph_api.components.fields.container_fields.ContainerFields` to get from the container, defaults to None
        :type fields: Optional[List[Union[str, ContainerFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{container-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint=f"/{container_id}", params=params)

    def create(self, *args, **kwargs):
        """ [Not Supported] Create an Instagram container.
        :raises InstagramApiEndpointError: Container creation is only supported by the User Media node
        """
        raise PystagramApiEndpointError(
            "Container creation is only supported by the User Media node, "
            "consider using the User Media node to create a container."
            "See the :class:`pystagram.graph_api.endpoints.user.media.Media` class for additional details."
        )

    def update(self, *args, **kwargs):
        """ [Not Supported] Update an Instagram comment.
        :raises InstagramApiNotSupportedError: Container update is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError(
            "Container update is not supported by the Instagram Graph API, "
            "container will expire after 24 hours."
        )

    def delete(self, *args, **kwargs):
        """ [Not Supported] Delete an Instagram comment.
        :raises InstagramApiNotSupportedError: Container deletion is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError(
            "Container deletion is not supported by the Instagram Graph API, "
            "container will expire after 24 hours."
        )
