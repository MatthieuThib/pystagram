from typing import List, Optional, Union

from pystagram.components.fields import MeFields
from pystagram.graph_api.endpoints.me.accounts import Accounts


class Me:
    """ The `Me` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `Me` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, fields: Optional[List[Union[str, MeFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on the User whose User Access Token is being used in the query.
        This endpoint translates to GET /{user-id}, based on the User ID identified by the access token used in the query.
        :param fields: A list of :class:`pystagram.graph_api.components.fields.me_fields.MeFields` to get from the User node, defaults to None
        :type fields: Optional[List[Union[str, MeFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /me` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint="/me", params=params)

    @property
    def accounts(self):
        """ The `Account` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.me.accounts.Accounts` class for additional details.
        """
        return Accounts(self)
