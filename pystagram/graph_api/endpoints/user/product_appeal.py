from typing import Optional


class ProductAppeal:
    """ The `ProductAppeal` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `ProductAppeal` node of the Instagram Graph API."""
        self.user = user

    def get(self, product_id: str, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get appeal status of a rejected product.
        :param product_id: The ID of the product to get appeal status from.
        :type product_id: str
        :param user_id: The ID of the user to get the appeal status from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/product_appeal` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "product_id": product_id,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/product_appeal", params=params)

    def create(self, appeal_reason: str, product_id: str, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Create an appeal for a rejected product.
        :param appeal_reason: The reason for the appeal.
        :type appeal_reason: str
        :param product_id: The ID of the product to appeal.
        :type product_id: str
        :param user_id: The ID of the user to appeal the product for, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `POST /{user-id}/product_appeal` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "appeal_reason": appeal_reason,
            "product_id": product_id,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="POST", endpoint=f"/{user_id}/product_appeal", params=params)
