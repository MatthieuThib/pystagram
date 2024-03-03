from enum import Enum

from pystagram.components.fields.base_fields import BaseFields


class Fields(str, Enum, metaclass=BaseFields):
    """ Base class for fields."""
    @classmethod
    def list(cls):
        """ Return a list of all fields values."""
        return list(map(lambda field: field.value, cls))
