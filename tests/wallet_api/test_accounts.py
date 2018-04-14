'''
pyburstlib
:author: drownedcoast
:date: 4-1-2018
'''
import pytest
from pyburstlib.wallet_api.models.accounts import *
from tests.base import BaseTest
from tests.config import PyBurstLibConfig

@pytest.mark.api
class TestAccountsApi(BaseTest):

    def setup(self):
        self.TEST_ACCOUNT_NUMERIC = PyBurstLibConfig.get('account_id')
        self.TEST_ACCOUNT_ADDRESS = PyBurstLibConfig.get('account_address')

    def test_accounts_get_account(self, client):
        account = client.wallet_accounts_api.get_account(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert account is not None
        assert isinstance(account, Account)
        assert account.account == self.TEST_ACCOUNT_NUMERIC

    def test_accounts_get_account_ATs(self, client):
        account_ATs = client.wallet_accounts_api.get_account_ATs(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(account_ATs, AccountATs)

    def test_accounts_get_account_block_ids(self, client):
        account_block_ids = client.wallet_accounts_api.get_account_block_ids(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(account_block_ids, AccountBlockIds)

    def test_accounts_get_account_blocks(self, client):
        account_blocks = client.wallet_accounts_api.get_account_blocks(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(account_blocks, AccountBlocks)

    def test_account_get_account_current_ask_order_ids(self, client):
        ask_order_ids = client.wallet_accounts_api.get_account_current_ask_order_ids(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(ask_order_ids, AccountCurrentAskOrderIds)

    def test_account_get_account_current_ask_orders(self, client):
        ask_orders = client.wallet_accounts_api.get_account_current_ask_orders(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(ask_orders, AccountCurrentAskOrders)
    
    def test_account_get_account_current_bid_order_ids(self, client):
        bid_order_ids = client.wallet_accounts_api.get_account_current_bid_order_ids(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(bid_order_ids, AccountCurrentBidOrderIds)

    def test_account_get_account_current_bid_orders(self, client):
        bid_orders = client.wallet_accounts_api.get_account_current_bid_orders(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(bid_orders, AccountCurrentBidOrders)

    def test_account_get_account_escrow_transactions(self, client):
        escrow_trx = client.wallet_accounts_api.get_account_escrow_transactions(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(escrow_trx, AccountEscrowTransactions)
    
    def test_account_get_account_id(self, client):
        test_pw = 'password'
        test_pub_key = '5e134ae913fb12b30dccee2aee9b53ddfc7710cf2405e348eb881b25252a2757'
        test_acct_numeric = '17946328911576397249'
        test_acct_rs = 'BURST-CXG3-3YUF-XQ85-HDK5L'
        acct_id = client.wallet_accounts_api.get_account_id(secret_pass=test_pw)
        assert isinstance(acct_id, AccountId)
        assert acct_id.account == test_acct_numeric
        assert acct_id.accountRS == test_acct_rs
        acct_id2 = client.wallet_accounts_api.get_account_id(public_key=test_pub_key)
        assert isinstance(acct_id2, AccountId)
        assert acct_id2.account == test_acct_numeric
        assert acct_id2.accountRS == test_acct_rs
        assert acct_id.account == acct_id2.account
    
    def test_account_get_account_lessors(self, client):
        acct_lessors = client.wallet_accounts_api.get_account_lessors(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(acct_lessors, AccountLessors)
    
    def test_account_get_account_public_key(self, client):
        pub_key = client.wallet_accounts_api.get_account_public_key(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(pub_key, AccountPublicKey)

    def test_account_get_account_subscriptions(self, client):
        subs = client.wallet_accounts_api.get_account_subscriptions(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(subs, AccountSubscriptions)
  
    def test_account_get_account_transaction_ids(self, client):
        trx_ids = client.wallet_accounts_api.get_account_transaction_ids(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(trx_ids, AccountTransactionIds)
        assert len(trx_ids.transactionIds) > 2  #Test account used must have transactions

    def test_account_get_account_transactions(self, client):
        trx = client.wallet_accounts_api.get_account_transactions(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(trx, AccountTransactions)
        assert isinstance(trx.transactions[0], TransactionJSON)
        assert len(trx.transactions) > 2 #Test account used must have transactions
    
    def test_account_get_accounts_with_reward_recipient(self, client):
        accts = client.wallet_accounts_api.get_accounts_with_reward_recipient(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(accts, Accounts)
        assert self.TEST_ACCOUNT_NUMERIC in accts.accounts

    def test_account_get_assets_by_issuer(self, client):
        assets = client.wallet_accounts_api.get_assets_by_issuer(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(assets, Assets)
    
    def test_account_get_balance(self, client):
        balance = client.wallet_accounts_api.get_balance(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(balance, Balance)
        assert int(balance.balanceNQT) > 0
    
    @pytest.mark.skip(reason='Not Implimented yet')
    def test_account_get_escrow_transactions(self, client):
        pass
    
    def test_account_get_guaranteed_balance(self, client):
        gbalance = client.wallet_accounts_api.get_guaranteed_balance(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(gbalance, GuaranteedBalance)
        assert int(gbalance.guaranteedBalanceNQT) > 0
    
    def test_account_get_reward_recipient(self, client):
        reward_recipient = client.wallet_accounts_api.get_reward_recipient(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(reward_recipient, RewardRecipient)
        assert reward_recipient.rewardRecipient == self.TEST_ACCOUNT_NUMERIC
    
    @pytest.mark.skip(reason='Was not able to set up subscription in testnet')
    def test_account_get_subscription(self, client):
        sub = client.wallet_accounts_api.get_subscription(subscription=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(sub, Subscription)

    def test_account_get_subscriptions_to_account(self, client):
        subs = client.wallet_accounts_api.get_subscriptions_to_account(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(subs, Subscriptions)
    
    def test_account_get_unconfirmed_transaction_ids(self, client):
        trx_ids = client.wallet_accounts_api.get_unconfirmed_transaction_ids(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(trx_ids, UnconfirmedTransactionIds)
    
    def test_account_get_unconfirmed_transactions(self, client):
        trx = client.wallet_accounts_api.get_unconfirmed_transactions(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(trx, UnconfirmedTransactions)
    
    def test_account_rs_convert(self, client):
        acct_rs = client.wallet_accounts_api.rs_convert(account_id=self.TEST_ACCOUNT_NUMERIC)
        assert isinstance(acct_rs, rsConvert)
        assert acct_rs.account == self.TEST_ACCOUNT_NUMERIC
        assert acct_rs.accountRS == self.TEST_ACCOUNT_ADDRESS

    def test_account_send_money(self, client):
        send_req = SendMoneyRequest(
            recipient=PyBurstLibConfig.get('account_address2'),
            amountNQT=100000000,
            secretPhrase=PyBurstLibConfig.get('account_pw')
        )
        send = client.wallet_accounts_api.send_money(req=send_req.as_dict())
        assert isinstance(send, SendMoneyResponse)
        assert isinstance(send.transactionJSON, TransactionJSON)
        assert send.transactionJSON.feeNQT == SendMoneyRequest.DEFAULT_SEND_MONEY_FEE
    
    @pytest.mark.skip(reason='Not Implimented yet')
    def test_set_account_info(self, client):
        pass

    def test_set_reward_recipient(self, client):
        reward_req = SetRewardRecipientRequest(
            recipient=PyBurstLibConfig.get('account_address'),
            secretPhrase=PyBurstLibConfig.get('account_pw')
        )
        set_reward = client.wallet_accounts_api.set_reward_recipient(req=reward_req.as_dict())
        assert isinstance(set_reward, SetRewardRecipientResponse)
        assert isinstance(set_reward.transactionJSON, TransactionJSON)
        assert set_reward.transactionJSON.feeNQT == SetRewardRecipientRequest.DEFAULT_REWARD_RECIPIENT_FEE

