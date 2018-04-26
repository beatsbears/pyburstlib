'''
pyburstlib
:author: drownedcoast
:date: 3-26-2018
'''
import datetime
from pyburstlib.wallet_api.base import BaseRequest
from pyburstlib.wallet_api.models.base import BaseModel

class Account(BaseModel):
    def __init__(
            self,
            unconfirmedBalanceNQT=None,
            guaranteedBalanceNQT=None,
            effectiveBalanceNXT=None,
            accountRS=None,
            name=None,
            description=None,
            forgedBalanceNQT=None,
            balanceNQT=None,
            publicKey=None,
            requestProcessingTime=None,
            account=None):
        self.unconfirmedBalanceNQT = unconfirmedBalanceNQT
        self.guaranteedBalanceNQT = guaranteedBalanceNQT
        self.effectiveBalanceNXT = effectiveBalanceNXT
        self.accountRS = accountRS
        self.name = name
        self.description = description
        self.forgedBalanceNQT = forgedBalanceNQT
        self.balanceNQT = balanceNQT
        self.publicKey = publicKey
        self.requestProcessingTime = requestProcessingTime
        self.account = account

class AccountATs(BaseModel):
    def __init__(
            self,
            ats=None,
            requestProcessingTime=None):
        self.ats = ats
        self.requestProcessingTime = requestProcessingTime

class AccountBlockIds(BaseModel):
    def __init__(
            self,
            blockIds=None,
            requestProcessingTime=None):
        self.blockIds = blockIds
        self.requestProcessingTime = requestProcessingTime

class AccountBlocks(BaseModel):
    def __init__(
            self,
            blocks=None,
            requestProcessingTime=None):
        self.blocks = blocks
        self.requestProcessingTime = requestProcessingTime

class AccountCurrentAskOrderIds(BaseModel):
    def __init__(
            self,
            askOrderIds=None,
            requestProcessingTime=None):
        self.askOrderIds = askOrderIds
        self.requestProcessingTime = requestProcessingTime

class AccountCurrentAskOrders(BaseModel):
    def __init__(
            self,
            askOrders=None,
            requestProcessingTime=None):
        self.askOrders = askOrders
        self.requestProcessingTime = requestProcessingTime

class AccountCurrentBidOrderIds(BaseModel):
    def __init__(
            self,
            bidOrderIds=None,
            requestProcessingTime=None):
        self.bidOrderIds = bidOrderIds
        self.requestProcessingTime = requestProcessingTime

class AccountCurrentBidOrders(BaseModel):
    def __init__(
            self,
            bidOrders=None,
            requestProcessingTime=None):
        self.bidOrders = bidOrders
        self.requestProcessingTime = requestProcessingTime

class AccountEscrowTransactions(BaseModel):
    def __init__(
            self,
            escrows=None,
            requestProcessingTime=None):
        self.escrows = escrows
        self.requestProcessingTime = requestProcessingTime

class AccountId(BaseModel):
    def __init__(
            self,
            accountRS=None,
            publicKey=None,
            account=None,
            requestProcessingTime=None):
        self.accountRS = accountRS
        self.publicKey = publicKey
        self.account = account
        self.requestProcessingTime = requestProcessingTime

class AccountLessors(BaseModel):
    def __init__(
            self,
            accountRS=None,
            lessors=None,
            account=None,
            requestProcessingTime=None):
        self.accountRS = accountRS
        self.lessors = lessors
        self.account = account
        self.requestProcessingTime = requestProcessingTime

class AccountPublicKey(BaseModel):
    def __init__(
            self,
            publicKey=None,
            requestProcessingTime=None):
        self.publicKey = publicKey
        self.requestProcessingTime = requestProcessingTime

class AccountSubscriptions(BaseModel):
    def __init__(
            self,
            subscriptions=None,
            requestProcessingTime=None):
        self.subscriptions = subscriptions
        self.requestProcessingTime = requestProcessingTime

class AccountTransactionIds(BaseModel):
    def __init__(
            self,
            transactionIds=None,
            requestProcessingTime=None):
        self.transactionIds = transactionIds
        self.requestProcessingTime = requestProcessingTime

class EncryptedMessage(BaseModel):
    def __init__(
            self,
            data=None,
            nonce=None,
            isText=None):
        self.data = data
        self.nonce = nonce
        self.isText = isText

class Attachment(BaseModel):
    def __init__(
            self,
            name=None,
            description=None,
            encryptedMessage=None):
        self._encryptedMessage = None

        self.name = name
        self.description = description
        self.encryptedMessage = encryptedMessage
    
    @property
    def encryptedMessage(self):
        return self._encryptedMessage

    @encryptedMessage.setter
    @BaseModel._model(EncryptedMessage)
    def encryptedMessage(self, encryptedMessage):
        self._encryptedMessage = encryptedMessage

class TransactionJSON(BaseModel):
    def __init__(
            self,
            senderPublicKey=None,
            feeNQT=None,
            type=None,
            version=None,
            ecBlockId=None,
            attachment=None,
            senderRS=None,
            subtype=None,
            amountNQT=None,
            sender=None,
            recipientRS=None,
            recipient=None,
            ecBlockHeight=None,
            deadline=None,
            timestamp=None,
            height=None):
        self._attachment = None

        self.senderPublicKey = senderPublicKey
        self.feeNQT = feeNQT
        self.type = type
        self.version = version
        self.ecBlockId = ecBlockId
        self.attachment = attachment
        self.senderRS = senderRS
        self.subtype = subtype
        self.amountNQT = amountNQT
        self.sender = sender
        self.recipientRS = recipientRS
        self.recipient = recipient
        self.ecBlockHeight = ecBlockHeight
        self.deadline = deadline
        self.timestamp = timestamp
        self.height = height

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    @BaseModel._model(Attachment)
    def attachment(self, attachment):
        self._attachment = attachment

class AccountTransactions(BaseModel):
    def __init__(
            self,
            transactions=None,
            requestProcessingTime=None):
        
        self._transactions = None
        self.transactions = transactions # will want to use a class here too
        self.requestProcessingTime = requestProcessingTime
    
    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    @BaseModel._model_list(TransactionJSON)
    def transactions(self, transactions):
        self._transactions = transactions

class Accounts(BaseModel):
    def __init__(
            self,
            accounts=None,
            requestProcessingTime=None):
        self.accounts = accounts
        self.requestProcessingTime = requestProcessingTime

class Assets(BaseModel):
    def __init__(
            self,
            assets=None,
            requestProcessingTime=None):
        self.assets = assets
        self.requestProcessingTime = requestProcessingTime

class Balance(BaseModel):
    def __init__(
            self,
            unconfirmedBalanceNQT=None,
            guaranteedBalanceNQT=None,
            effectiveBalanceNXT=None,
            forgedBalanceNQT=None,
            balanceNQT=None,
            requestProcessingTime=None):
        self.unconfirmedBalanceNQT = unconfirmedBalanceNQT
        self.guaranteedBalanceNQT = guaranteedBalanceNQT
        self.effectiveBalanceNXT = effectiveBalanceNXT
        self.forgedBalanceNQT = forgedBalanceNQT
        self.balanceNQT = balanceNQT
        self.requestProcessingTime = requestProcessingTime

class GuaranteedBalance(BaseModel):
    def __init__(
            self,
            guaranteedBalanceNQT=None,
            requestProcessingTime=None):
        self.guaranteedBalanceNQT = guaranteedBalanceNQT
        self.requestProcessingTime = requestProcessingTime

class RewardRecipient(BaseModel):
    def __init__(
            self,
            rewardRecipient=None,
            requestProcessingTime=None):
        self.rewardRecipient = rewardRecipient
        self.requestProcessingTime = requestProcessingTime

# TODO Investigate
class Subscription(BaseModel):
    def __init__(
            self,
            subscription=None,
            requestProcessingTime=None):
        self.subscription = subscription
        self.requestProcessingTime = requestProcessingTime

class Subscriptions(BaseModel):
    def __init__(
            self,
            subscriptions=None,
            requestProcessingTime=None):
        self.subscriptions = subscriptions
        self.requestProcessingTime = requestProcessingTime

class UnconfirmedTransactionIds(BaseModel):
    def __init__(
            self,
            unconfirmedTransactionIds=None,
            requestProcessingTime=None):
        self.unconfirmedTransactionIds = unconfirmedTransactionIds
        self.requestProcessingTime = requestProcessingTime

class UnconfirmedTransactions(BaseModel):
    def __init__(
            self,
            unconfirmedTransactions=None,
            requestProcessingTime=None):
        
        self._unconfirmedTransactions = None
        self.unconfirmedTransactions = unconfirmedTransactions
        self.requestProcessingTime = requestProcessingTime
    
    @property
    def unconfirmedTransactions(self):
        return self._unconfirmedTransactions

    @unconfirmedTransactions.setter
    @BaseModel._model_list(TransactionJSON)
    def unconfirmedTransactions(self, unconfirmedTransactions):
        self._unconfirmedTransactions = unconfirmedTransactions

class rsConvert(BaseModel):
    def __init__(
            self,
            account=None,
            accountRS=None,
            requestProcessingTime=None):
        self.account = account
        self.accountRS = accountRS
        self.requestProcessingTime = requestProcessingTime 
    
    @property
    def friendly(self):
        return self.accountRS 

class SendMoneyRequest(BaseRequest):
    '''

    '''

    DEFAULT_SEND_MONEY_FEE = '100000000'
    DEFAULT_SEND_MONEY_DEADLINE = '1440'
    def __init__(
            self, 
            recipient=None, 
            amountNQT=None, 
            secretPhrase=None, 
            publicKey=None,
            feeNQT=None, 
            deadline=None, 
            referencedTransactionFullHash=None, 
            broadcast=None,
            message=None, 
            messageIsText=None, 
            messageToEncrypt=None,
            messageToEncryptIsText=None,
            encryptedMessageData=None,
            encryptedMessageNonce=None,
            messageToEncryptToSelf=None,
            messageToEncryptToSelfIsText=None,
            encryptToSelfMessageData=None,
            encryptToSelfMessageNonce=None,
            recipientPublicKey=None):

        assert recipient is not None
        assert amountNQT is not None
        assert secretPhrase is not None
        if (feeNQT is not None and feeNQT < SendMoneyRequest.DEFAULT_SEND_MONEY_FEE):
            feeNQT = SendMoneyRequest.DEFAULT_SEND_MONEY_FEE # if fee is less than 1 BURST, set to 1
        self.recipient = recipient
        self.amountNQT = str(amountNQT)
        self.secretPhrase = secretPhrase
        self.publicKey = publicKey
        self.feeNQT = feeNQT if feeNQT else SendMoneyRequest.DEFAULT_SEND_MONEY_FEE
        self.deadline = deadline if deadline else SendMoneyRequest.DEFAULT_SEND_MONEY_DEADLINE
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast
        self.message = message
        self.messageIsText = messageIsText
        self.messageToEncrypt = messageToEncrypt
        self.messageToEncryptIsText = messageToEncryptIsText
        self.encryptedMessageData = encryptedMessageData
        self.encryptedMessageNonce = encryptedMessageNonce
        self.messageToEncryptToSelf = messageToEncryptToSelf
        self.messageToEncryptToSelfIsText = messageToEncryptToSelfIsText
        self.encryptToSelfMessageData = encryptToSelfMessageData
        self.encryptToSelfMessageNonce = encryptToSelfMessageNonce
        self.recipientPublicKey = recipientPublicKey
        self.requestType = 'sendMoney'

        def as_payload(self):
            return super(SendMoneyRequest, self).as_payload(True)

class SendMoneyResponse(BaseModel):
    def __init__(
            self,
            unsignedTransactionBytes=None,
            transactionJSON=None,
            broadcasted=None,
            transactionBytes=None,
            fullHash=None,
            transaction=None,
            signatureHash=None,
            requestProcessingTime=None):
        
        self._transactionJSON = None

        self.unsignedTransactionBytes = unsignedTransactionBytes
        self.transactionJSON = transactionJSON
        self.broadcasted = broadcasted
        self.transactionBytes = transactionBytes
        self.fullHash = fullHash
        self.transaction = transaction
        self.signatureHash = signatureHash
        self.requestProcessingTime = requestProcessingTime

    @property
    def transactionJSON(self):
        return self._transactionJSON

    @transactionJSON.setter
    @BaseModel._model(TransactionJSON)
    def transactionJSON(self, transactionJSON):
        self._transactionJSON = transactionJSON
    
class SetRewardRecipientRequest(BaseRequest):
    '''

    '''

    DEFAULT_REWARD_RECIPIENT_FEE = '100000000'
    DEFAULT_REWARD_RECIPIENT_DEADLINE = '1440'
    def __init__(
            self, 
            recipient=None, 
            amountNQT=None, 
            secretPhrase=None, 
            publicKey=None,
            feeNQT=None, 
            deadline=None, 
            referencedTransactionFullHash=None, 
            broadcast=None,
            message=None, 
            messageIsText=None, 
            messageToEncrypt=None,
            messageToEncryptIsText=None,
            encryptedMessageData=None,
            encryptedMessageNonce=None,
            messageToEncryptToSelf=None,
            messageToEncryptToSelfIsText=None,
            encryptToSelfMessageData=None,
            encryptToSelfMessageNonce=None,
            recipientPublicKey=None):

        assert recipient is not None
        assert secretPhrase is not None 
        if (feeNQT is not None and feeNQT < SetRewardRecipientRequest.DEFAULT_REWARD_RECIPIENT_FEE):
            feeNQT = SetRewardRecipientRequest.DEFAULT_REWARD_RECIPIENT_FEE # if fee is less than 1 BURST, set to 1
        self.recipient = recipient
        self.amountNQT = str(amountNQT)
        self.secretPhrase = secretPhrase
        self.publicKey = publicKey
        self.feeNQT = feeNQT if feeNQT else SetRewardRecipientRequest.DEFAULT_REWARD_RECIPIENT_FEE
        self.deadline = deadline if deadline else SetRewardRecipientRequest.DEFAULT_REWARD_RECIPIENT_DEADLINE
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast
        self.message = message
        self.messageIsText = messageIsText
        self.messageToEncrypt = messageToEncrypt
        self.messageToEncryptIsText = messageToEncryptIsText
        self.encryptedMessageData = encryptedMessageData
        self.encryptedMessageNonce = encryptedMessageNonce
        self.messageToEncryptToSelf = messageToEncryptToSelf
        self.messageToEncryptToSelfIsText = messageToEncryptToSelfIsText
        self.encryptToSelfMessageData = encryptToSelfMessageData
        self.encryptToSelfMessageNonce = encryptToSelfMessageNonce
        self.recipientPublicKey = recipientPublicKey
        self.requestType = 'setRewardRecipient'

        def as_payload(self):
            return super(SetRewardRecipientRequest, self).as_payload(True)

class SetRewardRecipientResponse(BaseModel):
    def __init__(
            self,
            unsignedTransactionBytes=None,
            transactionJSON=None,
            broadcasted=None,
            transactionBytes=None,
            fullHash=None,
            transaction=None,
            signatureHash=None,
            requestProcessingTime=None):
        
        self._transactionJSON = None

        self.unsignedTransactionBytes = unsignedTransactionBytes
        self.transactionJSON = transactionJSON
        self.broadcasted = broadcasted
        self.transactionBytes = transactionBytes
        self.fullHash = fullHash
        self.transaction = transaction
        self.signatureHash = signatureHash
        self.requestProcessingTime = requestProcessingTime

    @property
    def transactionJSON(self):
        return self._transactionJSON

    @transactionJSON.setter
    @BaseModel._model(TransactionJSON)
    def transactionJSON(self, transactionJSON):
        self._transactionJSON = transactionJSON

class SetAccountInfoRequest(BaseRequest):
    DEFAULT_ACCOUNT_INFO_FEE = '100000000'
    DEFAULT_ACCOUNT_INFO_DEADLINE = '1440'
    def __init__(
            self, 
            name=None,
            description=None,
            secretPhrase=None, 
            publicKey=None,
            feeNQT=None, 
            deadline=None, 
            referencedTransactionFullHash=None, 
            broadcast=None,
            message=None, 
            messageIsText=None, 
            messageToEncrypt=None,
            messageToEncryptIsText=None,
            encryptedMessageData=None,
            encryptedMessageNonce=None,
            messageToEncryptToSelf=None,
            messageToEncryptToSelfIsText=None,
            encryptToSelfMessageData=None,
            encryptToSelfMessageNonce=None,
            recipientPublicKey=None):

        assert secretPhrase is not None 
        if (feeNQT is not None and feeNQT < SetAccountInfoRequest.DEFAULT_ACCOUNT_INFO_FEE):
            feeNQT = SetAccountInfoRequest.DEFAULT_ACCOUNT_INFO_FEE # if fee is less than 1 BURST, set to 1
        self.name = name
        self.description = description
        self.secretPhrase = secretPhrase
        self.publicKey = publicKey
        self.feeNQT = feeNQT if feeNQT else SetAccountInfoRequest.DEFAULT_ACCOUNT_INFO_FEE
        self.deadline = deadline if deadline else SetAccountInfoRequest.DEFAULT_ACCOUNT_INFO_DEADLINE
        self.referencedTransactionFullHash = referencedTransactionFullHash
        self.broadcast = broadcast
        self.message = message
        self.messageIsText = messageIsText
        self.messageToEncrypt = messageToEncrypt
        self.messageToEncryptIsText = messageToEncryptIsText
        self.encryptedMessageData = encryptedMessageData
        self.encryptedMessageNonce = encryptedMessageNonce
        self.messageToEncryptToSelf = messageToEncryptToSelf
        self.messageToEncryptToSelfIsText = messageToEncryptToSelfIsText
        self.encryptToSelfMessageData = encryptToSelfMessageData
        self.encryptToSelfMessageNonce = encryptToSelfMessageNonce
        self.recipientPublicKey = recipientPublicKey
        self.requestType = 'setAccountInfo'

        def as_payload(self):
            return super(SetAccountInfoRequest, self).as_payload(True)

class SetAccountInfoResponse(BaseModel):
    def __init__(
            self,
            unsignedTransactionBytes=None,
            transactionJSON=None,
            broadcasted=None,
            transactionBytes=None,
            fullHash=None,
            transaction=None,
            signatureHash=None,
            requestProcessingTime=None):
        
        self._transactionJSON = None

        self.unsignedTransactionBytes = unsignedTransactionBytes
        self.transactionJSON = transactionJSON
        self.broadcasted = broadcasted
        self.transactionBytes = transactionBytes
        self.fullHash = fullHash
        self.transaction = transaction
        self.signatureHash = signatureHash
        self.requestProcessingTime = requestProcessingTime

    @property
    def transactionJSON(self):
        return self._transactionJSON

    @transactionJSON.setter
    @BaseModel._model(TransactionJSON)
    def transactionJSON(self, transactionJSON):
        self._transactionJSON = transactionJSON
