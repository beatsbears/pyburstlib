'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
from json import loads

from pyburstlib.wallet_api.base import BaseApi
from pyburstlib.wallet_api.models.utils import *
from pyburstlib.constants import BASE_WALLET_PATH

class UtilsApi(BaseApi):

    def rs_convert(self, account_id=None):
        '''
        Converts from numeric id to account address (rs format).

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`AccountRS`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'rsConvert',
                                           'account': account_id})
        return AccountRS.from_json(response.text)

    def long_convert(self, id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'longConvert',
                                           'id': id})
        return AccountLong.from_json(response.text)
