from typing import Optional


class CatalogProductSearch:
    """ The `CatalogProductSearch` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """

    def __init__(self, user: "User"):
        """ Initialize the `CatalogProductSearch` node of the Instagram Graph API."""
        self.user = user

    def get(self, catalog_id: int = None, q: Optional[str] = None, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get a collection of products that match a given search string within the targeted IG User's Instagram Shop catalog.
        :param catalog_id: The ID of the catalog to search products from, defaults to None
        :type catalog_id: int, optional
        :param q: The search string to match products with, defaults to None
        :type q: Optional[str], optional
        :param user_id: The ID of the user to search products from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/catalog_product_search` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "catalog_id": catalog_id,
            "q": q,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/catalog_product_search", params=params)
