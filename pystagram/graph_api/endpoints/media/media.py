from typing import List, Optional, Union

from pystagram.components.fields import MediaFields
from pystagram.graph_api.endpoints.media.children import Children
from pystagram.graph_api.endpoints.media.collaborators import Collaborators
from pystagram.graph_api.endpoints.media.comments import Comments
from pystagram.graph_api.endpoints.media.insights import Insights
from pystagram.graph_api.endpoints.media.product_tags import ProductTags
from pystagram.helpers.errors import (
    PystagramApiEndpointError,
    PystagramApiNotSupportedError,
)


class Media:
    """ The `Media` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `Media` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, media_id: str, fields: Optional[List[Union[str, MediaFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram media.
        :param media_id: The ID of the media to get fields and edges from.
        :type media_id: str
        :param fields: A list of :class:`pystagram.graph_api.components.fields.media_fields.MediaFields` to get from the media, defaults to None
        :type fields: Optional[List[Union[str, MediaFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint=f"/{media_id}", params=params)

    def create(self, *args, **kwargs):
        """ [Not Supported] Create an Instagram Media.
        :raises InstagramApiEndpointError: Media creation is only supported by the User Media node
        """
        raise PystagramApiEndpointError(
            "Media creation is only supported by the User Media node, "
            "consider using the User Media node to create a media."
            "See the :class:`pystagram.graph_api.endpoints.user.media.Media` class for additional details."
        )

    def update(self, media_id: str, comment_enabled: Optional[bool] = True, access_token: Optional[str] = None):
        """ Update an Instagram media. Only the `comment_enabled` field can be updated.
        :param media_id: The ID of the media to update.
        :type media_id: str
        :param comment_enabled: Whether comments are enabled on the media, defaults to True
        :type comment_enabled: Optional[bool], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        """
        params = {
            "comment_enabled": comment_enabled,
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="POST", endpoint=f"/{media_id}", params=params)

    def delete(self):
        """ [Not Supported] Delete an Instagram Media.
        :raises InstagramApiNotSupportedError: Instagram media deletion is not supported by the Instagram Graph API.
        """
        raise PystagramApiNotSupportedError("Media deletion is not supported by the Instagram Graph API")

    @property
    def children(self):
        """ The ``Children` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.media.children.Children` class for more information.
        """
        return Children(self)

    @property
    def collaborators(self):
        """ The `Collaborators` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.media.collaborators.Collaborators` class for more information.
        """
        return Collaborators(self)

    @property
    def comments(self):
        """ The `Comments` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.media.comments.Comments` class for more information.
        """
        return Comments(self)

    @property
    def insights(self):
        """ The `Insights` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.media.insights.Insights` class for more information.
        """
        return Insights(self)

    @property
    def product_tags(self):
        """ The `ProductTags` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.media.product_tags.ProductTags` class for more information.
        """
        return ProductTags(self)
