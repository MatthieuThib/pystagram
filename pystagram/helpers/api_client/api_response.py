from requests import Response


class PystagramApiResponse:
    def __init__(self, response: Response):
        self._response = response
        self.headers = response.headers
        self.url = response.url
        self.status_code = response.status_code
        self.text = response.text
        self.data = response.json()

    def __repr__(self):
        return f"InstagramApiResponse({self.status_code})"
