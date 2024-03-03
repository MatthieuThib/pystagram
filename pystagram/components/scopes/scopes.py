from enum import Enum, unique


@unique
class Scopes(str, Enum):
    """ Permissions to give to the app user. """
    USER_PROFILE = "user_profile"
    USER_MEDIA = "user_media"

    @classmethod
    def list(cls):
        """ Return a list of all fields values."""
        return list(map(lambda field: field.value, cls))
