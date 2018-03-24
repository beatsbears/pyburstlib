'''
pyburstlib
:author: drownedcoast
:date: 3-22-2018
'''
from json import loads

from pyburstlib.wallet_api.base import BaseApi
from pyburstlib.wallet_api.models.server import *
from pyburstlib.constants import BASE_WALLET_PATH

class ServerApi(BaseApi):

    def get_accounts_with_reward_recipient(self, account_id=None):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountsWithRewardRecipient',
                                           'account': account_id})
        return AccountsWithRewardRecipient.from_json(response.text)

    def get_blockchain_status(self):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getBlockchainStatus'})
        return BlockChainStatus.from_json(response.text)
    
    def get_constants(self):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getConstants'})
        return Constants.from_json(response.text)

    def get_mining_info(self):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getMiningInfo'})
        return MiningInfo.from_json(response.text)
    
    def get_my_info(self):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getMyInfo'})
        return MyInfo.from_json(response.text)

    def get_peer(self, peer=None):
        '''
        Peer is specified by IPv4 String or as IPv6 inside brackets
        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getPeer',
                                            'peer': peer})
        return Peer.from_json(response.text)

    def get_peers(self, active=1, state=None):
        '''
        defaults to active peers
        state appears not to work in my testing
        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getPeers',
                                            'active': active,
                                            'state': state})
        return Peers.from_json(response.text)

    def get_reward_recipient(self, account_id=None):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getRewardRecipient',
                                           'account': account_id})
        return RewardRecipient.from_json(response.text)
    
    def get_state(self, include_counts=None):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getState'})
        return State.from_json(response.text)
    
    def get_time(self):
        '''

        '''
        response = self._client.get(uri=BASE_WALLET_PATH, 
                                    params={'requestType': 'getTime'})
        return Time.from_json(response.text)