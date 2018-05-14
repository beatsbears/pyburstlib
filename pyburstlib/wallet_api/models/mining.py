'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
from pyburstlib.wallet_api.base import BaseRequest
from pyburstlib.wallet_api.models.base import BaseModel
from pyburstlib.wallet_api.accounts import TransactionJSON


class Accounts(BaseModel):
    def __init__(
            self,
            accounts=None,
            requestProcessingTime=None):
        self.accounts = accounts
        self.requestProcessingTime = requestProcessingTime
    
class MiningInfo(BaseModel):
    def __init__(
            self,
            generationSignature=None,
            baseTarget=None,
            requestProcessingTime=None,
            height=None):
        self.generationSignature = generationSignature
        self.baseTarget = baseTarget
        self.requestProcessingTime = requestProcessingTime
        self.height = height

class RewardRecipient(BaseModel):
    def __init__(
            self,
            rewardRecipient=None,
            requestProcessingTime=None):
        self.rewardRecipient = rewardRecipient
        self.requestProcessingTime = requestProcessingTime

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

class SubmitNonceResponse(BaseModel):

    SUCCESS = 'success'

    def __init__(
            self,
            result=None,
            deadline=None,
            requestProcessingTime=None):
        self.result = result
        self.deadline = deadline
        self.requestProcessingTime = requestProcessingTime