'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
import pytest
from pyburstlib.wallet_api.models.mining import *
from tests.base import BaseTest
from tests.config import PyBurstLibConfig

@pytest.mark.api
class TestMiningApi(BaseTest):

    def setup(self):
        self.TEST_ACCOUNT_NUMERIC = PyBurstLibConfig.get('account_id')
        self.TEST_ACCOUNT_ADDRESS = PyBurstLibConfig.get('account_address')
    
    def test_mining_get_accounts_with_reward_recipient(self, client):
        accts = client.wallet_mining_api.get_accounts_with_reward_recipient(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(accts, Accounts)
        assert self.TEST_ACCOUNT_NUMERIC in accts.accounts

    def test_mining_get_mining_info(self, client):
        info = client.wallet_mining_api.get_mining_info()
        assert isinstance(info, MiningInfo)

    def test_mining_get_reward_recipient(self, client):
        reward = client.wallet_mining_api.get_reward_recipient(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(reward, RewardRecipient)
        assert self.TEST_ACCOUNT_NUMERIC == reward.rewardRecipient

    def test_mining_set_reward_recipient(self, client):
        reward_req = SetRewardRecipientRequest(
            recipient=PyBurstLibConfig.get('account_address'),
            secretPhrase=PyBurstLibConfig.get('account_pw')
        )
        set_reward = client.wallet_mining_api.set_reward_recipient(req=reward_req.as_dict())
        assert isinstance(set_reward, SetRewardRecipientResponse)
        assert isinstance(set_reward.transactionJSON, TransactionJSON)
        assert set_reward.transactionJSON.feeNQT == SetRewardRecipientRequest.DEFAULT_REWARD_RECIPIENT_FEE

    def test_mining_submit_nonce(self, client):
        nonce = client.wallet_mining_api.submit_nonce(secret_pass=PyBurstLibConfig.get('account_pw'),
                                                      nonce="100000",
                                                      account_id=PyBurstLibConfig.get('account_id'))
        assert isinstance(nonce, SubmitNonceResponse)
        assert nonce.result == SubmitNonceResponse.SUCCESS