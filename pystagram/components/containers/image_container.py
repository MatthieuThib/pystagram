from typing import List, Optional

from pystagram.components.containers.base_container import BaseContainer
from pystagram.components.media_type.media_type import MediaType
from pystagram.components.tags.product_tag import ProductTag
from pystagram.components.tags.user_tag import UserTag


class ImageContainer(BaseContainer):
    """ Instagram Image Container.

    :param image_url: URL of the image, image must be hosted on a publicly accessible server.
    :type image_url: str
    :param is_carousel_item: Whether th image will appear in a carousel, defaults to False.
    :type is_carousel_item: Optional[bool], optional
    :param caption: Caption for the image.
    :type caption: Optional[str], optional
    :param collaborators: List of collaborators.
    :type collaborators: Optional[List[str]], optional
    :param location_id: Location ID.
    :type location_id: Optional[str], optional
    :param user_tags: List of user tags.
    :type user_tags: Optional[List[UserTag]], optional
    :param product_tags: Product tags.
    :type product_tags: Optional[List[ProductTag]], optional
    """
    def __init__(
        self,
        image_url: str,
        is_carousel_item: Optional[bool] = False,
        caption: Optional[str] = None,
        collaborators: Optional[List[str]] = None,
        location_id: Optional[str] = None,
        user_tags: Optional[List[UserTag]] = None,
        product_tags: Optional[List[ProductTag]] = None,
    ):
        """ Initialize an ImageContainer."""
        super().__init__()
        self.media_type = MediaType.IMAGE
        self.image_url = image_url
        self.is_carousel_item = is_carousel_item
        self.caption = caption
        self.collaborators = collaborators
        self.location_id = location_id
        self.user_tags = user_tags
        self.product_tags = product_tags
