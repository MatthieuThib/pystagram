from enum import Enum

from pystagram.components.metrics.base_metrics import BaseMetrics


class Metrics(str, Enum, metaclass=BaseMetrics):
    """ Base class for metrics."""
    @classmethod
    def list(cls):
        """ Return a list of all metrics values."""
        return list(map(lambda field: field.value, cls))
