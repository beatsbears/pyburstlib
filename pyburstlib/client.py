'''
pyburstlib
:author: drownedcoast
:date: 3-21-2018
'''
import requests
import sys
import json

from requests.packages.urllib3 import Retry
from requests.utils import quote

from pyburstlib.config import PyBurstLibConfig
from pyburstlib.exceptions import BurstAPIException
from pyburstlib.log import format_request, logging

# base request
from pyburstlib.wallet_api.base import BaseRequest

# wallet ais
from pyburstlib.wallet_api.server import ServerApi

class BurstAPIClient(object):

    _MAX_RETRIES = PyBurstLibConfig.get('max_retries')
    _TOTAL_RETRIES = _MAX_RETRIES if int(_MAX_RETRIES) < 10 else 10
    _RETRY_STATUS_CODES = {429, 500, 501, 502, 503, 504}

    def __init__(
            self,
            node_url=PyBurstLibConfig.get('node_url'),
            node_port=PyBurstLibConfig.get('node_port')
    ):
        self._node_url = node_url
        self._node_port = node_port

        self._init_api()
        self._init_session()
        # self._init_helpers()

    def _init_api(self):
        '''
        Initializes all apis
        '''
        self.wallet_server_api = ServerApi(self)

    def _init_helpers(self):
        '''
        Initializes all helpers.
        '''
        pass
    
    def _init_session(self):
        '''
        Initializes the requests session
        '''
        retries = Retry(
                    total=int(BurstAPIClient._TOTAL_RETRIES),
                    status_forcelist=BurstAPIClient._RETRY_STATUS_CODES,
                    backoff_factor=2,
                    respect_retry_after_header=True
        )
        adapter = requests.adapters.HTTPAdapter(max_retries=retries)
        self._session = requests.Session()
        self._session.mount('http://', adapter)
        self._session.mount('https://', adapter)
        self._session.headers.update({
            u'User-Agent': u'pyburstlib Python/%s' % ('.'.join([str(i) for i in sys.version_info][0:3]))
        })

    def _error_handler(f):
        '''
        Decorator to handle response error.
        :param f: Response returning method.
        :return: A Response returning method that raises PyBurstLibException for error in response.
        '''
        def wrapper(*args, **kwargs):
            response = f(*args, **kwargs)
            if not 200 <= response.status_code <= 299:
                raise BurstAPIException(response)
            if 'errorCode' in json.loads(response.text):
                raise BurstAPIException(response)
            return response
        return wrapper

    @_error_handler
    def get(self, uri, path_params=None, **kwargs):
        return self._request('GET', uri, path_params, **kwargs)

    @_error_handler
    def post(self, uri, payload=None, path_params=None, **kwargs):
        if isinstance(payload, BaseRequest):
            payload = payload.as_payload()
        return self._request('POST', uri, path_params, json=payload, **kwargs)

    @_error_handler
    def put(self, uri, payload=None, path_params=None, **kwargs):
        if isinstance(payload, BaseRequest):
            payload = payload.as_payload()
        return self._request('PUT', uri, path_params, json=payload, **kwargs)

    @_error_handler
    def delete(self, uri, path_params=None, **kwargs):
        return self._request('DELETE', uri, path_params, **kwargs)

    @classmethod
    def _flatten_param(cls, params):
        '''
        Flatten the query params to be compatible with the API.
        :param params: The params object to process.
        :return: Nested dict/list values are flatten into single level dict.
        '''
        flatten = params
        if type(params) in [dict, list]:
            flatten = {}
            for k, v in (params.items() if type(params) is dict else enumerate(params)):
                f = cls._flatten_param(v)
                if type(f) is dict:
                    for kk, vv in f.items():
                        flatten[u'%s.%s' % (k, kk)] = vv
                else:
                    flatten[k] = v
        return flatten

    def _request(self, method, uri, path_params=None, flatten_params=True, **kwargs):
        if path_params:
            # Ensure path param is encoded.
            path_params = {key: quote(str(value), safe=u'') for key, value in path_params.items()}
            uri %= path_params

        # Custom nested object flattening
        if flatten_params and 'params' in kwargs:
            kwargs['params'] = self._flatten_param(kwargs['params'])

        full_uri = '{}:{}'.format(self._node_url, self._node_port) + uri

        response = self._session.request(method, full_uri, **kwargs)
        log_message = format_request(response)

        logging.info(log_message)
        if not 200 <= response.status_code <= 299:
            logging.error(log_message)

        return response

    # Delayed qualifying decorator as staticmethod. This is a workaround to error raised from using a decorator
    # decorated by @staticmethod.
    _error_handler = staticmethod(_error_handler)