from enum import unique

from pystagram.components.metrics.metrics import Metrics


@unique
class ReelMetrics(Metrics):
    CLIPS_REPLAYS_COUNT = "clips_replays_count"
    COMMENTS = "comments"
    IG_REELS_AGGREGATED_ALL_PLAYS_COUNT = "ig_reels_aggregated_all_plays_count"
    IG_REELS_AVG_WATCH_TIME = "ig_reels_avg_watch_time"
    IG_REELS_VIDEO_VIEW_TOTAL_TIME = "ig_reels_video_view_total_time"
    LIKES = "likes"
    PLAYS = "plays"
    REACH = "reach"
    SAVED = "saved"
    SHARES = "shares"
    TOTAL_INTERACTIONS = "total_interactions"
