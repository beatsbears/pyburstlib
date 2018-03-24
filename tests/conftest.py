'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''
import os
import pytest
import shutil
import uuid
from tests.base import BaseTest
from pyburstlib.client import BurstAPIClient

class Tester:
    def __init__(self):
        self._output_dir = self.session_name('./._tests_')
        os.makedirs(self._output_dir)

    def session_name(self, name, length=8):
        return uuid.uuid4()

    def session_file_output(self, name, content=None):
        path = u'%s/%s' % (self._output_dir, name)
        if content:
            with open(path, 'a') as fd:
                fd.write('test_file')
        return path

    def tear_down(self):
        shutil.rmtree(self._output_dir)

@pytest.fixture(scope='session')
def tester():
    t = Tester()
    yield t
    t.tear_down()

@pytest.fixture(scope='session')
def client():
    yield BurstAPIClient()
