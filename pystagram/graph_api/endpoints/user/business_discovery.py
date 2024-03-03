from typing import List, Optional, Union

from pystagram.components.fields import UserFields


class BusinessDiscovery:
    """ The `BusinessDiscovery` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `BusinessDiscovery` node of the Instagram Graph API."""
        self.user = user

    def get(self, username: str, fields: Optional[List[Union[str, UserFields]]] = None, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get data about another Instagram Business or Creator Instagram User.
        :param username: The username of the Instagram Business or Creator Instagram User.
        :type username: str
        :param fields: A list of :class:`pystagram.graph_api.components.fields.user_fields.UserFields` to get from the user, defaults to None
        :type fields: Optional[List[Union[str, UserFields]]], optional
        :param user_id: The ID of the user to get fields and edges from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        username = username.replace("@", "")
        params = {
            "fields": "business_discovery.username({}){{{}}}".format(username, fields),
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}", params=params)
