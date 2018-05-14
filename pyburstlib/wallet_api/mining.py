'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
from json import loads

from pyburstlib.wallet_api.base import BaseApi
from pyburstlib.wallet_api.models.mining import *
from pyburstlib.constants import BASE_WALLET_PATH

class MiningApi(BaseApi):

    def get_accounts_with_reward_recipient(self, account_id=None):
        '''
        Takes a numeric account id as an argument and returns a list of accounts that have 
        the original account as their reward recipient.

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`AccountsWithRewardRecipient`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountsWithRewardRecipient',
                                           'account': account_id})
        return Accounts.from_json(response.text)
    
    def get_mining_info(self):
        '''
        Returns information related to mining.

        :returns: An instance of :class:`MiningInfo`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getMiningInfo'})
        return MiningInfo.from_json(response.text)

    def get_reward_recipient(self, account_id=None):
        '''
        Returns the reward recipient for an account.

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`RewardRecipient`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getRewardRecipient',
                                           'account': account_id})
        return RewardRecipient.from_json(response.text)

    def set_reward_recipient(self, req: SetRewardRecipientRequest=None):
        '''
        Sets the reward recipient for an account

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`RewardRecipient`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, params=req)
        return SetRewardRecipientResponse.from_json(response.text)

    def submit_nonce(self, secret_pass=None, nonce=None, account_id=None):
        '''
        Submits a nonce as part of the mining process.

        :param secret_pass: The secret phrase for the submitting account.
        :type secret_pass: str
        :param nonce: Nonce to submit
        :type nonce: str
        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`SubmitNonceResponse`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'submitNonce',
                                           'secretPhrase': secret_pass,
                                           'nonce': nonce,
                                           'accountId': account_id})
        return SubmitNonceResponse.from_json(response.text)