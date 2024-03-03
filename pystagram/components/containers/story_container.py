from typing import Optional

from pystagram.components.containers.base_container import BaseContainer
from pystagram.components.media_type.media_type import MediaType


class StoryContainer(BaseContainer):
    """ Instagram Story Container.

    :param image_url: URL of the image, image must be hosted on a publicly accessible server.
    :type image_url: str
    :param video_url: URL of the video, video must be hosted on a publicly accessible server.
    :type video_url: str
    :param reel_url: URL of the reel, reel must be hosted on a publicly accessible server.
    :type reel_url: str
    """
    def __init__(
        self,
        image_url: Optional[str] = None,
        video_url: Optional[str] = None,
        reel_url: Optional[str] = None
    ):
        """ Initialize a StoryContainer."""
        super().__init__()
        self.media_type = MediaType.STORIES
        if sum(media_url is not None for media_url in [image_url, video_url, reel_url]) != 1:
            raise ValueError("Exactly one media_url (image_url, video_url, or reel_url) should be provided.")
        if image_url is not None:
            self.image_url = image_url
        if video_url is not None:
            self.video_url = video_url
        if reel_url is not None:
            self.reel_url = reel_url
