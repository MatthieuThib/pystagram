from typing import List, Optional, Union

from pystagram.components.fields import AccountFields


class Accounts:
    """ The `Accounts` node of the Instagram Graph API.
    :param me: An instance of the :class:`Me` class.
    :type me: :class:`Me`
    """
    def __init__(self, me: "Me"):
        """ Initialize the `Accounts` node of the Instagram Graph API."""
        self.me = me

    def get(self, fields: Optional[List[Union[str, AccountFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on the facebook User accounts whose User Access Token is being used in the query.
        This endpoint translates to GET /{user-id}/accounts, based on the User ID identified by the access token used in the query.
        :param fields: A list of :class:`pystagram.graph_api.components.fields.account_fields.AccountFields` to get from the Accounts node, defaults to None
        :type fields: Optional[List[Union[str, AccountFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /me/accounts` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.me.graph_api._access_token,
        }
        return self.me.graph_api.api_request(method="GET", endpoint="/me/accounts", params=params)
