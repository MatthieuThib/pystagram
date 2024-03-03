from enum import unique

from pystagram.components.metrics.metrics import Metrics


@unique
class AlbumMetrics(Metrics):
    CAROUSEL_ALBUM_ENGAGEMENT = "carousel_album_engagement"
    CAROUSEL_ALBUM_IMPRESSIONS = "carousel_album_impressions"
    CAROUSEL_ALBUM_REACH = "carousel_album_reach"
    CAROUSEL_ALBUM_SAVED = "carousel_album_saved"
    CAROUSEL_ALBUM_VIDEO_VIEWS = "carousel_album_video_views"
