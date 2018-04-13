'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''
import configparser
from os import environ

base_config = {
    'wait_timeout': environ.get('TEST_WAIT_TIMEOUT', '300'),
    'node_url': environ.get('NODE_URL', 'http://176.9.47.157'),
    'node_port': environ.get('NODE_PORT', 6876),
    'account_pw': environ.get('PYBURSTLIB_ACCOUNT_PW', '')
}

# Read pyburstlib.ini config and defaults to environment variables if available
config = configparser.SafeConfigParser(base_config)
config.add_section('test')
config.read('pyburstlib.ini')

class PyBurstLibConfig(object):

    @staticmethod
    def get(key):
        return config.get('test', key)