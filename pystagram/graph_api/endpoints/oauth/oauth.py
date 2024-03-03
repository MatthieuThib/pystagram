from pystagram.graph_api.endpoints.oauth.access_token import AccessToken


class Oauth:
    """ The `Oauth` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initializes the `Oauth` class."""
        self.graph_api = graph_api

    @property
    def access_token(self):
        """ The `AccessToken` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.oauth.access_token.access_token.AccessToken` class for additional details.
        """
        return AccessToken(self)
