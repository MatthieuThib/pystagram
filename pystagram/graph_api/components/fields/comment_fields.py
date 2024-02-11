from enum import unique

from pystagram.graph_api.components.fields.fields import Fields


@unique
class CommentFields(Fields):
    ID = "id"
    LIKE_COUNT = "like_count"
    MEDIA = "media"
    TEXT = "text"
    TIMESTAMP = "timestamp"
