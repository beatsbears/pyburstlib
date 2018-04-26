'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
import pytest
from pyburstlib.wallet_api.models.utils import *
from tests.base import BaseTest
from tests.config import PyBurstLibConfig

@pytest.mark.api
class TestUtilsApi(BaseTest):

    def setup(self):
        self.TEST_ACCOUNT_NUMERIC = PyBurstLibConfig.get('account_id')
        self.TEST_ACCOUNT_ADDRESS = PyBurstLibConfig.get('account_address')

    def test_rs_convert(self, client):
        rs_format = client.wallet_utils_api.rs_convert(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(rs_format, AccountRS)
        assert rs_format.accountRS == self.TEST_ACCOUNT_ADDRESS

    def test_long_convert(self, client):
        long_format = client.wallet_utils_api.long_convert(id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(long_format, AccountLong)
        assert long_format.stringId == self.TEST_ACCOUNT_NUMERIC