
class PystagramApiError(Exception):
    pass


class PystagramApiNotSupportedError(PystagramApiError):
    pass


class PystagramApiEndpointError(PystagramApiError):
    pass
