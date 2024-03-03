from pystagram.basic_display_api.endpoints.oauth.access_token import AccessToken
from pystagram.basic_display_api.endpoints.oauth.authorize.authorize import Authorize


class Oauth:
    """ The `Oauth` node of the Instagram Basic Display API.
    :param basic_display_api: An instance of the :class:`PystagramBasicDisplayApi` class.
    :type basic_display_api: :class:`PystagramBasicDisplayApi`
    """
    def __init__(self, basic_display_api: "PystagramBasicDisplayApi"):
        """ Initializes the `Oauth` class."""
        self.basic_display_api = basic_display_api

    @property
    def access_token(self):
        """ The `AccessToken` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.oauth.access_token.access_token.AccessToken` class for additional details.
        """
        return AccessToken(self)

    @property
    def authorize(self):
        """ The `Authorize` node of the Instagram Basic Display API.
        See the :class:`pystagram.basic_display_api.endpoints.oauth.authorize.authorize.Authorize` class for additional details.
        """
        return Authorize(self)
