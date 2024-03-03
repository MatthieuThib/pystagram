from typing import List, Optional, Union

from pystagram.components.fields import CatalogFields


class AvailableCatalogs:
    """ The `AvailableCatalogs` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `AvailableCatalogs` node of the Instagram Graph API."""
        self.user = user

    def get(self, user_id: Optional[str] = None, fields: Optional[List[Union[str, CatalogFields]]] = None, access_token: Optional[str] = None):
        """ Get the product catalog in an IG User's Instagram Shop.
        :param user_id: The ID of the user to get available catalogs from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param fields: A list of :class:`pystagram.graph_api.components.fields.catalog_fields.CatalogFields` to get from the available catalogs, defaults to None
        :type fields: Optional[List[Union[str, CatalogFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/available_catalogs` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/available_catalogs", params=params)
