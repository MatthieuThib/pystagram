from enum import Enum


class Periods(str, Enum):
    """ Instagram periods."""
    LIFETIME = "lifetime"
    DAY = "day"
    DAYS_28 = "days_28"
    WEEK = "week"

    @classmethod
    def list(cls):
        """ Return a list of all periods values."""
        return list(map(lambda period: period.value, cls))
