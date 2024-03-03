from enum import Enum, unique


@unique
class Breakdown(str, Enum):
    """ Designates how to break down a result set into subsets."""
    ACTION_TYPE = "action_type"
    STORY_NAVIGATION_ACTION_TYPE = "story_navigation_action_type"
