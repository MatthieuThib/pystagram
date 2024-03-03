from enum import unique

from pystagram.components.fields.fields import Fields


@unique
class UserFields(Fields):
    BIO = "bio"
    BUSINESS_ACCOUNT = "business_account"
    FOLLOWERS_COUNT = "followers_count"
    FOLLOWING_COUNT = "following_count"
    ID = "id"
    IS_PRIVATE = "is_private"
    IS_VERIFIED = "is_verified"
    MEDIA_COUNT = "media_count"
    NAME = "name"
    PROFILE_PICTURE_URL = "profile_picture_url"
    USERNAME = "username"
    WEBSITE = "website"
