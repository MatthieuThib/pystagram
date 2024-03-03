from typing import List, Optional, Union

from pystagram.components.fields import UserFields
from pystagram.graph_api.endpoints.user.available_catalogs import AvailableCatalogs
from pystagram.graph_api.endpoints.user.business_discovery import BusinessDiscovery
from pystagram.graph_api.endpoints.user.catalog_product_search import CatalogProductSearch
from pystagram.graph_api.endpoints.user.content_publishing_limit import ContentPublishingLimit
from pystagram.graph_api.endpoints.user.insights import Insights
from pystagram.graph_api.endpoints.user.live_media import LiveMedia
from pystagram.graph_api.endpoints.user.media import Media
from pystagram.graph_api.endpoints.user.media_publish import MediaPublish
from pystagram.graph_api.endpoints.user.mentionned_comment import MentionedComment
from pystagram.graph_api.endpoints.user.mentionned_media import MentionedMedia
from pystagram.graph_api.endpoints.user.mentions import Mentions
from pystagram.graph_api.endpoints.user.product_appeal import ProductAppeal
from pystagram.graph_api.endpoints.user.recently_searched_hashtags import RecentlySearchedHashtags
from pystagram.graph_api.endpoints.user.stories import Stories
from pystagram.graph_api.endpoints.user.tags import Tags


class User:
    """ The `User` node of the Instagram Graph API.
    :param graph_api: An instance of the :class:`PystagramGraphApi` class.
    :type graph_api: :class:`PystagramGraphApi`
    """
    def __init__(self, graph_api: "PystagramGraphApi"):
        """ Initialize the `User` node of the Instagram Graph API."""
        self.graph_api = graph_api

    def get(self, user_id: Optional[str] = None, fields: Optional[List[Union[str, UserFields]]] = None, access_token: Optional[str] = None):
        """ Get fields and edges on an Instagram Business or Creator Account.
        :param user_id: The ID of the user to get fields and edges from, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type user_id: str, optional
        :param fields: A list of :class:`pystagram.graph_api.components.fields.user_fields.UserFields` to get from the user, defaults to None
        :type fields: Optional[List[Union[str, UserFields]]], optional
        :param access_token: The access token of the Instagram user, inferred from the `PystagramGraphApi` instance if None, defaults to None
        :type access_token: str, optional
        :return: The response from the `GET /{user-id}` endpoint.
        :rtype: :class:`pystagram.helpers.api_client.api_response.PystagramApiResponse`
        """
        user_id = user_id or self.graph_api.user_id
        params = {
            "fields": None if fields is None else (fields if isinstance(fields, str) else ",".join(fields)),
            "access_token": access_token or self.graph_api._access_token,
        }
        return self.graph_api.api_request(method="GET", endpoint=f"/{user_id}", params=params)

    @property
    def available_catalogs(self):
        """ The `AvailableCatalogs` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.available_catalogs.AvailableCatalogs` class for additional details.
        """
        return AvailableCatalogs(self)

    @property
    def business_discovery(self):
        """ The `BusinessDiscovery` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.business_discovery.BusinessDiscovery` class for additional details.
        """
        return BusinessDiscovery(self)

    @property
    def catalog_product_search(self):
        """ The `CatalogProductSearch` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.catalog_product_search.CatalogProductSearch` class for additional details.
        """
        return CatalogProductSearch(self)

    @property
    def content_publishing_limit(self):
        """ The `ContentPublishingLimit` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.content_publishing_limit.ContentPublishingLimit` class for additional details.
        """
        return ContentPublishingLimit(self)

    @property
    def insights(self):
        """ The `Insights` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.insights.Insights` class for additional details.
        """
        return Insights(self)

    @property
    def live_media(self):
        """ The `LiveMedia` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.live_media.LiveMedia` class for additional details.
        """
        return LiveMedia(self)

    @property
    def media(self):
        """ The `Media` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.media.Media` class for additional details.
        """
        return Media(self)

    @property
    def media_publish(self):
        """ The `MediaPublish` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.media_publish.MediaPublish` class for additional details.
        """
        return MediaPublish(self)

    @property
    def mentions(self):
        """ The `Mentions` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.mentions.Mentions` class for additional details.
        """
        return Mentions(self)

    @property
    def mentioned_comment(self):
        """ The `MentionedComment` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.mentionned_comment.MentionedComment` class for additional details.
        """
        return MentionedComment(self)

    @property
    def mentioned_media(self):
        """ The `MentionedMedia` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.mentionned_media.MentionedMedia` class for additional details.
        """
        return MentionedMedia(self)

    @property
    def product_appeal(self):
        """ The `ProductAppeal` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.product_appeal.ProductAppeal` class for additional details.
        """
        return ProductAppeal(self)

    @property
    def recently_searched_hashtags(self):
        """ The `RecentlySearchedHashtags` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.recently_searched_hashtags.RecentlySearchedHashtags` class for additional details.
        """
        return RecentlySearchedHashtags(self)

    @property
    def stories(self):
        """ The `Stories` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.stories.Stories` class for additional details.
        """
        return Stories(self)

    @property
    def tags(self):
        """ The `Tags` node of the Instagram Graph API.
        See the :class:`pystagram.graph_api.endpoints.user.tags.Tags` class for additional details.
        """
        return Tags(self)
