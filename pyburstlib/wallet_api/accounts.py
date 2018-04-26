'''
pyburstlib
:author: drownedcoast
:date: 3-26-2018
'''
from json import loads

from pyburstlib.wallet_api.base import BaseApi, BaseRequest
from pyburstlib.wallet_api.models.accounts import *
from pyburstlib.constants import BASE_WALLET_PATH

class AccountsApi(BaseApi):

    def get_account(self, account_id=None):
        '''
        Gets account details.

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`Account`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccount',
                                           'account': account_id})
        return Account.from_json(response.text)

    def get_account_ATs(self, account_id=None):
        '''
        Gets account ATs.

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`AccountATs`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountATs',
                                           'account': account_id})
        return AccountATs.from_json(response.text)

    def get_account_block_ids(self, account_id=None, timestamp=None, first_index=None, last_index=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountBlockIds',
                                           'account': account_id,
                                           'timestamp': timestamp,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index})
        return AccountBlockIds.from_json(response.text)

    def get_account_blocks(self, account_id=None, timestamp=None, first_index=None, last_index=None, include_transactions=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountBlockIds',
                                           'account': account_id,
                                           'timestamp': timestamp,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index,
                                           'includeTransactions': include_transactions})
        return AccountBlocks.from_json(response.text)
    
    def get_account_current_ask_order_ids(self, account_id=None, asset=None, first_index=None, last_index=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountCurrentAskOrderIds',
                                           'account': account_id,
                                           'asset': asset,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index})
        return AccountCurrentAskOrderIds.from_json(response.text)

    def get_account_current_ask_orders(self, account_id=None, asset=None, first_index=None, last_index=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountCurrentAskOrders',
                                           'account': account_id,
                                           'asset': asset,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index})
        return AccountCurrentAskOrders.from_json(response.text)

    def get_account_current_bid_order_ids(self, account_id=None, asset=None, first_index=None, last_index=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountCurrentBidOrderIds',
                                           'account': account_id,
                                           'asset': asset,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index})
        return AccountCurrentBidOrderIds.from_json(response.text)

    def get_account_current_bid_orders(self, account_id=None, asset=None, first_index=None, last_index=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountCurrentBidOrders',
                                           'account': account_id,
                                           'asset': asset,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index})
        return AccountCurrentBidOrders.from_json(response.text)

    def get_account_escrow_transactions(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountEscrowTransactions',
                                           'account': account_id})
        return AccountEscrowTransactions.from_json(response.text)

    def get_account_id(self, secret_pass=None, public_key=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountId',
                                           'secretPhrase': secret_pass,
                                           'publicKey': public_key})
        return AccountId.from_json(response.text)
    
    def get_account_lessors(self, account_id=None, height=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountLessors',
                                           'account': account_id,
                                           'height': height})
        return AccountLessors.from_json(response.text)

    def get_account_public_key(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountPublicKey',
                                           'account': account_id})
        return AccountPublicKey.from_json(response.text)

    def get_account_subscriptions(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountSubscriptions',
                                           'account': account_id})
        return AccountSubscriptions.from_json(response.text)

    def get_account_transaction_ids(self, account_id=None, timestamp=None, _type=None, 
                                    subtype=None, first_index=None, last_index=None, 
                                    number_of_confirmations=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountTransactionIds',
                                           'account': account_id,
                                           'timestamp': timestamp,
                                           'type': _type,
                                           'subtype': subtype,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index,
                                           'numberOfConfirmations': number_of_confirmations})
        return AccountTransactionIds.from_json(response.text)

    def get_account_transactions(self, account_id=None, timestamp=None, _type=None, 
                                    subtype=None, first_index=None, last_index=None, 
                                    number_of_confirmations=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountTransactions',
                                           'account': account_id,
                                           'timestamp': timestamp,
                                           'type': _type,
                                           'subtype': subtype,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index,
                                           'numberOfConfirmations': number_of_confirmations})
        return AccountTransactions.from_json(response.text)

    def get_accounts_with_reward_recipient(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAccountsWithRewardRecipient',
                                           'account': account_id})
        return Accounts.from_json(response.text)

    def get_assets_by_issuer(self, account_id=None, first_index=None, last_index=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getAssetsByIssuer',
                                           'account': account_id,
                                           'firstIndex': first_index,
                                           'lastIndex': last_index})
        return Assets.from_json(response.text)

    def get_balance(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getBalance',
                                           'account': account_id})
        return Balance.from_json(response.text)
        
    def get_escrow_transactions(self, escrow=None):
        '''

        '''
        #TODO Find and Test
        pass

    def get_guaranteed_balance(self, account_id=None, number_of_confirmations=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getGuaranteedBalance',
                                           'account': account_id,
                                           'numberOfConfirmations': number_of_confirmations})
        return GuaranteedBalance.from_json(response.text)
    
    def get_reward_recipient(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getRewardRecipient',
                                           'account': account_id})
        return RewardRecipient.from_json(response.text)

    def get_subscription(self, subscription=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getSubscription',
                                           'subscription': subscription})
        return Subscription.from_json(response.text)

    def get_subscriptions_to_account(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getSubscriptionsToAccount',
                                           'account': account_id})
        return Subscriptions.from_json(response.text)

    def get_unconfirmed_transaction_ids(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getUnconfirmedTransactionIds',
                                           'account': account_id})
        return UnconfirmedTransactionIds.from_json(response.text)
    
    def get_unconfirmed_transactions(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'getUnconfirmedTransactions',
                                           'account': account_id})
        return UnconfirmedTransactions.from_json(response.text)
    
    def rs_convert(self, account_id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'rsConvert',
                                           'account': account_id})
        return rsConvert.from_json(response.text)
    
    def send_money(self, req: SendMoneyRequest=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, params=req)
        return SendMoneyResponse.from_json(response.text)

    def set_account_info(self, req: SetAccountInfoRequest=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, params=req)
        return SetAccountInfoResponse.from_json(response.text)

    def set_reward_recipient(self, req: SetRewardRecipientRequest=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, params=req)
        return SetRewardRecipientResponse.from_json(response.text)
