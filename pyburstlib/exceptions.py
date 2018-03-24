class PyBurstLibException(Exception):

    def __init__(self, message=None, code=None):
        self.code = code if code else BurstAPIErrorCode.GENERIC
        self.message = message if message else self.code.description

    def __str__(self):
        return self.message


class BurstAPIException(PyBurstLibException):

    def __init__(self, response):
        self.response = response
        code = BurstAPIErrorCode.from_http_code(response.status_code)
        if code:
            super(BurstAPIException, self).__init__(
                response.text if response.text else code.description,
                code
            )
        else:
            super(BurstAPIException, self).__init__(response.text)


class ErrorCode(object):

    _HTTP_CODES = {}

    def __init__(self, description, http_code=None):
        self.description = description
        self._http_code = http_code
        if self._http_code:
            ErrorCode._HTTP_CODES[self._http_code] = self

    @staticmethod
    def from_http_code(code):
        return ErrorCode._HTTP_CODES.get(code)

    def __str__(self):
        return self.description


class BurstAPIErrorCode(ErrorCode):

    GENERIC = ErrorCode("Generic")

    OK = ErrorCode("OK", 200)
    CREATED = ErrorCode("Created", 201)
    ACCEPTED = ErrorCode("Accepted", 202)
    NO_CONTENT = ErrorCode("No Content", 204)
    MOVED_PERMANENTLY = ErrorCode("Moved Permanently", 301)
    FOUND = ErrorCode("Found", 302)
    TEMPORARY_REDIRECT = ErrorCode("Temporary Redirect", 307)
    PERMANENT_REDIRECT = ErrorCode("Permanent Redirect", 308)
    BAD_REQUEST = ErrorCode("Bad Request", 400)
    UNAUTHORIZED = ErrorCode("Unauthorized", 401)
    NOT_FOUND = ErrorCode("Not Found", 404)
    METHOD_NOT_ALLOWED = ErrorCode("Method Not Allowed", 405)
    NOT_ACCEPTABLE = ErrorCode("Not Acceptable", 406)
    PROXY_AUTHENTICATION_REQUIRED = ErrorCode("Proxy Authentication Required", 407)
    REQUEST_TIMEOUT = ErrorCode("Request Timeout", 408)
    CONFLICT = ErrorCode("Conflict", 409)
    GONE = ErrorCode("Gone", 410)
    PAYLOAD_TOO_LARGE = ErrorCode("Payload Too Large", 413)
    IM_A_TEAPOT = ErrorCode("I'm a teapot", 418) #lol
    UNPROCESSABLE_ENTITY = ErrorCode("Unprocessable Entity", 422)
    LOCKED = ErrorCode("Locked", 423)
    FAILED_DEPENDENCY = ErrorCode("Failed Dependency", 424)
    UPGRADE_REQUIRED = ErrorCode("Upgrade Required", 426)
    TOO_MANY_REQUESTS = ErrorCode("Too Many Requests", 429)
    CLIENT_CLOSED_REQUEST = ErrorCode("Client Closed Request", 499)
    INTERNAL_SERVER_ERROR = ErrorCode("Internal Server Error", 500)
    NOT_IMPLEMENTED = ErrorCode("Not Implemented", 501)
    BAD_GATEWAY = ErrorCode("Bad Gateway", 502)
    SERVICE_UNAVAILABLE = ErrorCode("Service Unavailable", 503)
    GATEWAY_TIMEOUT = ErrorCode("Gateway Timeout", 504)
    HTTP_VERSION_NOT_SUPPORTED = ErrorCode("HTTP Version Not Supported", 505)
