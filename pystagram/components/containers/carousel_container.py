from typing import List, Optional

from pystagram.components.containers.base_container import BaseContainer
from pystagram.components.media_type.media_type import MediaType


class CarouselContainer(BaseContainer):
    """ Instagram Carousel Container.

    :param children: List of children containers.
    :type children: List[BaseContainer]
    :param caption: Caption for the carousel.
    :type caption: Optional[str]
    """
    def __init__(self, children: List[BaseContainer], caption: Optional[str] = None):
        """ Initialize a CarouselContainer."""
        super().__init__()
        self.media_type = MediaType.CAROUSEL
        self.children = children
        self.caption = caption
