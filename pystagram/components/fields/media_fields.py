from enum import unique

from pystagram.components.fields.fields import Fields


@unique
class MediaFields(Fields):
    CAPTION = "caption"
    CHILDREN = "children"
    COMMENTS_COUNT = "comments_count"
    COPYRIGHT_CHECK_INFORMATION = "copyright_check_information"
    ID = "id"
    IG_ID = "ig_id"
    IS_COMMENT_ENABLED = "is_comment_enabled"
    IS_SHARED_TO_FEED = "is_shared_to_feed"
    LIKE_COUNT = "like_count"
    MEDIA_PRODUCT_TYPE = "media_product_type"
    MEDIA_TYPE = "media_type"
    MEDIA_URL = "media_url"
    OWNER = "owner"
    PERMALINK = "permalink"
    SHORTCODE = "shortcode"
    THUMBNAIL_URL = "thumbnail_url"
    TIMESTAMP = "timestamp"
    USERNAME = "username"
