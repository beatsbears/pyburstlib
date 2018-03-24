'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''
import pytest
from pyburstlib.wallet_api.models.server import *
from tests.base import BaseTest

@pytest.mark.api
class TestServerApi(BaseTest):

    def test_server_get_time(self, client):
        server_time = client.wallet_server_api.get_time()
        assert isinstance(server_time, Time)
