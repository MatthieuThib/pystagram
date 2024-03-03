from typing import List, Optional

from pystagram.components.containers.base_container import BaseContainer
from pystagram.components.media_type.media_type import MediaType
from pystagram.components.tags.user_tag import UserTag


class ReelContainer(BaseContainer):
    """ Instagram Reel Container.

    :param video_url: URL of the video, video must be hosted on a publicly accessible server.
    :type video_url: str
    :param share_to_feed: Whether to share the reel to the feed, defaults to True.
    :type share_to_feed: Optional[bool], optional
    :param caption: Caption for the reel.
    :type caption: Optional[str], optional
    :param collaborators: List of collaborators.
    :type collaborators: Optional[List[str]], optional
    :param cover_url: URL of the cover image, cover image must be hosted on a publicly accessible server.
    :type cover_url: Optional[str], optional
    :param audio_name: Name of the audio.
    :type audio_name: Optional[str], optional
    :param user_tags: List of user tags.
    :type user_tags: Optional[List[UserTag]], optional
    :param location_id: Location ID.
    :type location_id: Optional[str], optional
    :param thumb_offset: Thumbnail offset.
    :type thumb_offset: Optional[int], optional
    """
    def __init__(
        self,
        video_url: str,
        share_to_feed: Optional[bool] = True,
        caption: Optional[str] = None,
        collaborators: Optional[List[str]] = None,
        cover_url: Optional[str] = None,
        audio_name: Optional[str] = None,
        user_tags: Optional[List[UserTag]] = None,
        location_id: Optional[str] = None,
        thumb_offset: Optional[int] = 0,
    ):
        """ Initialize a ReelContainer."""
        super().__init__()
        self.media_type = MediaType.REEL
        self.video_url = video_url
        self.share_to_feed = share_to_feed
        self.caption = caption
        self.collaborators = collaborators
        self.cover_url = cover_url
        self.audio_name = audio_name
        self.user_tags = user_tags
        self.location_id = location_id
        self.thumb_offset = thumb_offset
