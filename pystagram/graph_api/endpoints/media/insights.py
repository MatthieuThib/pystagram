from typing import List, Optional

from pystagram.components.breakdown import Breakdown
from pystagram.components.metrics import InsightMetrics


class Insights:
    """ The `Insights` node of the Instagram Graph API.
    :param media: An instance of the :class:`Media` class.
    :type media: :class:`Media`
    """
    def __init__(self, media: "Media"):
        """ Initialize the `Insights` node of the Instagram Graph API."""
        self.media = media

    def get(self, media_id: str, metrics: Optional[List[InsightMetrics]] = None, breakdown: Optional[Breakdown] = None, access_token: Optional[str] = None):
        """ Get insights data on an Instagram media.
        :param media_id: The ID of the media to get insights data from.
        :type media_id: str
        :param metrics: A list of :class:`pystagram.graph_api.components.metrics.insight_metrics.InsightMetrics` to get from the media, defaults to None
        :type metrics: Optional[List[InsightMetrics]], optional
        :param breakdown: The breakdown of the insights data, defaults to None
        :type breakdown: Optional[Breakdown], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{media-id}/insights` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "metric": ",".join(metrics),
            "breakdown": breakdown,
            "access_token": access_token or self.media.graph_api._access_token,
        }
        return self.media.graph_api.api_request(method="GET", endpoint=f"/{media_id}/insights", params=params)
