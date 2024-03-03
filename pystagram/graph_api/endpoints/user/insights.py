from typing import List, Optional, Union

from pystagram.components.metrics import InsightMetrics
from pystagram.components.periods import Periods
from pystagram.components.strtotime import Strtotime
from pystagram.components.timestamp import Timestamp
from pystagram.helpers.decorators import cursor_paginated


class Insights:
    """ The `Insights` node of the Instagram Graph API.
    :param user: An instance of the :class:`User` class.
    :type user: :class:`User`
    """
    def __init__(self, user: "User"):
        """ Initialize the `Insights` node of the Instagram Graph API."""
        self.user = user

    @cursor_paginated
    def get(self, metric: List[InsightMetrics], period: Periods, since: Optional[Union[Timestamp, Strtotime]] = None, until: Optional[Union[Timestamp, Strtotime]] = None, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get insights on an Instagram user

        :param metric: A list of :class:`pystagram.graph_api.components.metrics.insight_metrics.InsightMetrics` to get insights on.
        :type metric: List[InsightMetrics]
        :param period: The period of time to get insights from.
        :type period: Periods
        :param since: The start time of the insights, defaults to None
        :type since: Optional[Union[Timestamp, Strtotime]], optional
        :param until: The end time of the insights, defaults to None
        :type until: Optional[Union[Timestamp, Strtotime]], optional
        :param user_id: The ID of the user to get insights from, inferred from the `User` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}/insights` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.user.graph_api.user_id
        params = {
            "metric": metric,
            "period": period,
            "since": since,
            "until": until,
            "access_token": access_token or self.user.graph_api._access_token,
        }
        return self.user.graph_api.api_request(method="GET", endpoint=f"/{user_id}/insights", params=params)
