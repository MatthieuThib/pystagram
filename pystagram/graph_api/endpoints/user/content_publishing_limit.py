from typing import List, Optional, Union

from pystagram.components.fields import PublishingLimitFields
from pystagram.components.strtotime import Strtotime
from pystagram.components.timestamp import Timestamp


class ContentPublishingLimit:
    """ The `ContentPublishingLimit` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `ContentPublishingLimit` node of the Instagram Graph API."""
        self.user = user

    def get(self, user_id: Optional[str] = None, fields: Optional[List[Union[str, PublishingLimitFields]]] = None, since: Optional[Union[Timestamp, Strtotime]] = None, access_token: Optional[str] = None):
        """ Get the number of times an IG User has published and IG Container within a given time period.
        :param user_id: The ID of the user to get the content publishing limit from, inferred from the `User` instance if None, defaults to None
        :type user_id: str, optional
        :param fields: A list of :class:`pystagram.graph_api.components.fields.publishing_limit_fields.PublishingLimitFields` to get from the user, defaults to None
        :type fields: Optional[List[Union[str, PublishingLimitFields]]], optional
        :param since: The start time to get the content publishing limit from, defaults to None
        :type since: Optional[Union[Timestamp, Strtotime]], optional
        :param access_token: The access token of the Instagram user, inferred from the `User` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/content_publishing_limit` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "since": since,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/content_publishing_limit", params=params)
