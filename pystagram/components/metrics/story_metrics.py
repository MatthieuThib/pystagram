from enum import unique

from pystagram.components.metrics.metrics import Metrics


@unique
class StoryMetrics(Metrics):
    EXITS = "exits"
    IMPRESSIONS = "impressions"
    REACH = "reach"
    REPLIES = "replies"
    TAPS_FORWARD = "taps_forward"
    TAPS_BACK = "taps_back"
