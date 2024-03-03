from typing import Optional


class HashtagSearch:
    """ The `HashtagSearch` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `HashtagSearch` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, q: str, user_id: Optional[str] = None, access_token: Optional[str] = None):
        """ Get the id of an Instagram hashtag. IDs are both static and global (i.e, the ID for #bluebottle will always be 17843857450040591 for all apps and all app users).
        :param q: The hashtag to search for.
        :type q: str
        :param user_id: The ID of the Instagram user to get recent media from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /hashtag_search` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        params = {
            "q": q.replace("#", ""),
            "user_id": user_id or self.graph_api.user_id,
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint=f"/ig_hashtag_search", params=params)
