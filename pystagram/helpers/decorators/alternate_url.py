from functools import wraps
from typing import Callable

from pystagram.helpers.api_client import PystagramApiResponse


def alternate_url(endpoint_func: Callable[..., PystagramApiResponse]):
    @wraps(endpoint_func)
    def wrapper(self, *args, **kwargs):
        base_url: str = self.base_url
        self.base_url = self.ALTERNATE_URL
        result = endpoint_func(self, *args, **kwargs)
        self.base_url = base_url
        return result
    return wrapper
