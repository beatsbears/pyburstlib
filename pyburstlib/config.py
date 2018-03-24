'''
pyburstlib
:author: drownedcoast
:date: 3-21-2018
'''
import configparser
from os import environ

base_config = {
    'node_url': environ.get('NODE_URL', 'http://localhost'),
    'node_port': environ.get('NODE_PORT', 8125),
    'explorer_url': environ.get('EXPLORER_URL', 'http://localhost'),
    'explorer_port': environ.get('EXPLORER_PORT', 8125),
    'pool_url': environ.get('POOL_URL', 'http://localhost'),
    'pool_port': environ.get('POOL_PORT', 8124),
    'logging_level': environ.get('PYBURSTLIB_LOGGING_LEVEL', 'WARNING'),
    'max_retries': environ.get('PYBURSTLIB_MAX_RETRIES', '3'),
}

# Read pyburstlib.ini config. Default to environment variables if exist.
config = configparser.SafeConfigParser(base_config)
config.add_section('default')
config.read('pyburstlib.ini')

class PyBurstLibConfig(object):

    @staticmethod
    def get(key):
        return config.get('default', key)