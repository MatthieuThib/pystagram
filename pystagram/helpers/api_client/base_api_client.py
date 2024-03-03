from typing import Any, Dict

from requests import HTTPError, request

from pystagram.helpers.api_client import PystagramApiResponse
from pystagram.helpers.errors import (
    PystagramApiError,
    PystagramApiRequestError,
    PystagramOAuthError,
)


class PystagramBaseApiClient:
    """A base class for making requests to an API."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def api_request(self, method: str, endpoint: str, params: Dict[str, Any]):
        try:
            response = request(
                url=self.base_url + endpoint, method=method, params=params
            )
            if response.json().get("error"):
                raise PystagramOAuthError(response.json().get("error"))
            response.raise_for_status()
        except PystagramOAuthError as err:
            raise err
        except HTTPError as err:
            raise PystagramApiRequestError(err)
        except Exception as err:
            raise PystagramApiError(err)

        return PystagramApiResponse(response)
