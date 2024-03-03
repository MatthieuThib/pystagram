from enum import Enum, unique


@unique
class MediaType(str, Enum):
    """ Media type available in Instagram."""
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    REEL = "REEL"
    STORIES = "STORIES"
    CAROUSEL = "CAROUSEL"
