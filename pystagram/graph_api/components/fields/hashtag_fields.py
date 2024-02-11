from enum import unique

from pystagram.graph_api.components.fields.fields import Fields


@unique
class HashtagFields(Fields):
    ID = "id"
    NAME = "name"
