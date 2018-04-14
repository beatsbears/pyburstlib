'''
pyburstlib
:author: drownedcoast
:date: 3-24-2018
'''
import pytest
from pyburstlib.wallet_api.models.server import *
from tests.base import BaseTest
from tests.config import PyBurstLibConfig

@pytest.mark.api
class TestServerApi(BaseTest):

    def setup(self):
        self.TEST_ACCOUNT_NUMERIC = PyBurstLibConfig.get('account_id')

    def test_server_get_time(self, client):
        server_time = client.wallet_server_api.get_time()
        assert isinstance(server_time, Time)
    
    def test_server_get_state(self, client):
        state = client.wallet_server_api.get_state()
        assert isinstance(state, State)
        assert state.lastBlock is not None
        assert state.numberOfBlocks is not None

    def test_server_get_blockchain_status(self, client):
        status = client.wallet_server_api.get_blockchain_status()
        assert isinstance(status, BlockchainStatus)
        assert status.numberOfBlocks is not None
        assert status.lastBlock is not None
        assert status.cumulativeDifficulty is not None
        assert status.time is not None

    def test_server_get_mining_info(self, client):
        mining_info = client.wallet_server_api.get_mining_info()
        assert isinstance(mining_info, MiningInfo)
        assert mining_info.height is not None
        assert mining_info.generationSignature is not None

    def test_server_get_constants(self, client):
        constants = client.wallet_server_api.get_constants()
        assert isinstance(constants, Constants)
        assert constants.maxArbitraryMessageLength is not None
        assert constants.transactionTypes[0].subtypes[0].value is not None
    
    def test_server_get_peers(self, client):
        peers = client.wallet_server_api.get_peers()
        assert isinstance(peers, Peers)
        assert len(peers.peers) > 2

        peer_details = client.wallet_server_api.get_peer(peers.peers[0])   
        assert isinstance(peer_details, Peer)
        assert peer_details.lastUpdated is not None

    def test_server_get_reward_recipient(self, client):
        reward_recipient = client.wallet_server_api.get_reward_recipient(self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(reward_recipient, RewardRecipient)
        assert reward_recipient.rewardRecipient is not None
        
        recipient_list = client.wallet_server_api.get_accounts_with_reward_recipient(reward_recipient.rewardRecipient)
        assert isinstance(recipient_list, AccountsWithRewardRecipient)
        assert self.TEST_ACCOUNT_NUMERIC in recipient_list.accounts 
