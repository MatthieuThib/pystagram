from enum import unique

from pystagram.components.metrics.metrics import Metrics


@unique
class InsightMetrics(Metrics):
    AUDIENCE_CITY = "audience_city"
    AUDIENCE_COUNTRY = "audience_country"
    AUDIENCE_GENDER_AGE = "audience_gender_age"
    AUDIENCE_LOCALE = "audience_locale"
    EMAIL_CONTACTS = "email_contacts"
    FOLLOWER_COUNT = "follower_count"
    GET_DIRECTIONS_CLICKS = "get_directions_clicks"
    IMPRESSIONS = "impressions"
    ONLINE_FOLLOWERS = "online_followers"
    PHONE_CALL_CLICKS = "phone_call_clicks"
    PROFILE_VIEWS = "profile_views"
    REACH = "reach"
    TEXT_MESSAGE_CLICKS = "text_message_clicks"
    WEBSITE_CLICKS = "website_clicks"
