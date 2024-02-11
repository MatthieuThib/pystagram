from enum import unique

from pystagram.graph_api.components.fields.fields import Fields


@unique
class PublishingLimitFields(Fields):
    CONFIG = "config"
    QUOTA_USAGE = "quota_usage"
