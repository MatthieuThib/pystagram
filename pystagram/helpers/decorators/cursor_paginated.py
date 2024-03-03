from functools import wraps
from typing import Callable, Optional

from pystagram.helpers.api_client import PystagramApiResponse


def cursor_paginated(endpoint_func: Callable[..., PystagramApiResponse]):
    @wraps(endpoint_func)
    def wrapper(self, *args, **kwargs):
        response: PystagramApiResponse = endpoint_func(self, *args, **kwargs)
        page: int = 1
        after: Optional[str] = (response.data
                                .get("paging", dict())
                                .get("cursors", dict())
                                .get("after"))
        while after and (self.max_pages is None or page < self.max_pages):
            response = endpoint_func(self, *args, **kwargs, after=after)
            response.data["data"].extend(response.data.get("data", list()))
            page += 1
        return response
    return wrapper
