'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''
from time import sleep, time
from tests.config import PyBurstLibConfig

WAIT_TIMEOUT = int(PyBurstLibConfig.get('wait_timeout'))

class BaseTest(object):

    def setup_method(self, method):
        if not hasattr(self, '_timer'):
            self._timer = {}
        print("\n%s:%s is running." % (type(self).__name__, method.__name__))
        self._timer[method.__name__] = time()

    def teardown_method(self, method):
        duration = time() - self._timer[method.__name__]
        print("\n%s:%s took (%s seconds)." % (type(self).__name__, method.__name__, duration))