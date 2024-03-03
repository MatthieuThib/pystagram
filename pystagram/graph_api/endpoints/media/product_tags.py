from typing import List, Optional

from pystagram.components.tags import ProductTag


class ProductTags:
    """ The `ProductTags` node of the Instagram Graph API.
    :param media: An instance of the :class:`Media` class.
    :type media: :class:`Media`
    """
    def __init__(self, media: "Media"):
        """ Initialize the `ProductTags` node of the Instagram Graph API."""
        self.media = media

    def get(self, media_id: str, access_token: Optional[str] = None):
        """ Get a collection of product tags on an Instagram Media.
        :param media_id: The ID of the media to get product tags from.
        :type media_id: str
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}/product_tags` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="GET", endpoint=f"/{media_id}/product_tags", params=params)

    def create(self, media_id: str, product_tags: List[ProductTag], access_token: Optional[str] = None):
        """ Create product tags on an existing Instagram Media.
        :param media_id: The ID of the media to create product tags on.
        :type media_id: str
        :param product_tags: A list of :class:`pystagram.graph_api.components.tags.product_tag.ProductTag` objects to create on the media.
        :type product_tags: List[ProductTag]
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{media-id}/product_tags` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "updated_tags": [product_tag.dict() for product_tag in product_tags],
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="POST", endpoint=f"/{media_id}/product_tags", params=params)

    def update(self, media_id: str, product_tags: List[ProductTag], access_token: Optional[str] = None):
        """ Alias for the `create` method."""
        return self.media.graph_api.product_tag_create(media_id=media_id, product_tags=product_tags, access_token=access_token)

    def delete(self, media_id: str, product_tags: List[ProductTag], access_token: Optional[str] = None):
        """ Delete product tags on an existing Instagram Media.
        :param media_id: The ID of the media to delete product tags from.
        :type media_id: str
        :param product_tags: A list of :class:`pystagram.graph_api.components.tags.product_tag.ProductTag` objects to delete from the media.
        :type product_tags: List[ProductTag]
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `DELETE /{media-id}/product_tags` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "deleted_tags": [product_tag.dict() for product_tag in product_tags],
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="DELETE", endpoint=f"/{media_id}/product_tags", params=params)
