"""
**Instagram Basic Display API**
The Instagram Basic Display API allows users of your app to get basic profile information, photos, and videos
 in their Instagram accounts.The API can be used to access any type of Instagram account but only provides
 read-access to basic data. If you are building an app that will allow Instagram Businesses or Creators
 to publish media, moderate comments, identify @mentioned and hashtagged media, or get data about other
 Instagram users, use the Instagram Graph API instead.
"""

from pystagram.helpers.api_client.base_api_client import PystagramBaseApiClient


class PystagramBasicDisplayApi(PystagramBaseApiClient):
    raise NotImplementedError
