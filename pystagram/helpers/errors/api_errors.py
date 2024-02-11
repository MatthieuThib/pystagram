from requests import HTTPError, Timeout


class PystagramApiTimeoutError(Timeout):
    pass


class PystagramApiRequestError(HTTPError):
    pass


class PystagramOAuthError(PystagramApiRequestError):
    def __init__(self, error: dict):
        self.__dict__.update(error)
        super().__init__(str(self.__dict__))
