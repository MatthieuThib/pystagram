from enum import unique

from pystagram.graph_api.components.metrics.metrics import Metrics


@unique
class MediaMetrics(Metrics):
    ENGAGEMENT = "engagement"
    IMPRESSIONS = "impressions"
    REACH = "reach"
    SAVED = "saved"
    VIDEO_VIEWS = "video_views"
