from abc import ABCMeta
from enum import EnumMeta


class BaseMetrics(ABCMeta, EnumMeta):
    """ Metaclass for metrics."""
    pass
