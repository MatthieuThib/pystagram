from enum import unique

from pystagram.components.fields.fields import Fields


@unique
class HashtagFields(Fields):
    ID = "id"
    NAME = "name"
