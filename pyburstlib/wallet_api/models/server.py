'''
pyburstlib
:author: drownedcoast
:date: 3-23-2018
'''
import datetime
from pyburstlib.wallet_api.models.base import BaseModel

class AccountsWithRewardRecipient(BaseModel):
    def __init__(
            self,
            accounts=None,
            requestProcessingTime=None):
        self.accounts = accounts
        self.requestProcessingTime = requestProcessingTime

class BlockChainStatus(BaseModel):
    def __init__(
            self,
            lastBlock=None,
            application=None,
            isScanning=None,
            cumulativeDifficulty=None,
            lastBlockchainFeederHeight=None,
            numberOfBlocks=None,
            time=None,
            requestProcessingTime=None,
            version=None,
            lastBlockchainFeeder=None):
        self.lastBlock = lastBlock
        self.application = application
        self.isScanning = isScanning
        self.cumulativeDifficulty = cumulativeDifficulty
        self.lastBlockchainFeederHeight = lastBlockchainFeederHeight
        self.numberOfBlocks = numberOfBlocks
        self.time = time
        self.requestProcessingTime = requestProcessingTime
        self.version = version
        self.lastBlockchainFeeder = lastBlockchainFeeder

class Constants(BaseModel):
    def __init__(
            self,
            maxBlockPayloadLength=None,
            genesisAccountId=None,
            genesisBlockId=None,
            transactionTypes=None,
            peerStates=None,
            maxArbitraryMessageLength=None,
            requestTypes=None):
        self.maxBlockPayloadLength = maxBlockPayloadLength
        self.genesisAccountId = genesisAccountId
        self.genesisBlockId = genesisBlockId
        self.transactionTypes = transactionTypes
        self.peerStates = peerStates
        self.maxArbitraryMessageLength = maxArbitraryMessageLength
        self.requestTypes = requestTypes

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

class MyInfo(BaseModel):
    def __init__(
            self,
            address=None,
            host=None,
            requestProcessingTime=None):
        self.address = address
        self.host = host
        self.requestProcessingTime = requestProcessingTime

class Peer(BaseModel):
    def __init__(
            self,
            lastUpdated=None,
            downloadedVolume=None,
            blacklisted=None,
            announcedAddress=None,
            application=None,
            weight=None,
            uploadedVolume=None,
            state=None,
            requestProcessingTime=None,
            version=None,
            platform=None,
            shareAddress=None):
        self.lastUpdated = lastUpdated
        self.downloadedVolume = downloadedVolume
        self.blacklisted = blacklisted
        self.announcedAddress = announcedAddress
        self.application = application
        self.weight = weight
        self.uploadedVolume = uploadedVolume
        self.state = state
        self.requestProcessingTime = requestProcessingTime
        self.version = version
        self.platform = platform
        self.shareAddress = shareAddress

class Peers(BaseModel):
    def __init__(
            self,
            peers=None):
        self.peers = peers

class RewardRecipient(BaseModel):
    def __init__(
            self,
            rewardRecipient=None,
            requestProcessingTime=None):
        self.rewardRecipient = rewardRecipient
        self.requestProcessingTime = requestProcessingTime

class State(BaseModel):
    def __init__(
            self,
            numberOfPeers=None,
            numberOfUnlockedAccounts=None,
            numberOfTransfers=None,
            numberOfOrders=None,
            numberOfTransactions=None,
            maxMemory=None,
            isScanning=None,
            cumulativeDifficulty=None,
            numberOfAssets=None,
            freeMemory=None,
            availableProcessors=None,
            totalEffectiveBalanceNXT=None, #did this change in 2.0.0?
            numberOfAccounts=None,
            numberOfBlocks=None,
            requestProcessingTime=None,
            version=None,
            numberOfBidOrders=None,
            lastBlock=None,
            totalMemory=None,
            application=None,
            numberOfAliases=None,
            lastBlockchainFeederHeight=None,
            numberOfTrades=None,
            time=None,
            numberOfAskOrders=None,
            lastBlockchainFeeder=None):
        self.numberOfPeers = numberOfPeers
        self.numberOfUnlockedAccounts = numberOfUnlockedAccounts
        self.numberOfTransfers = numberOfTransfers
        self.numberOfOrders = numberOfOrders
        self.numberOfTransactions = numberOfTransactions
        self.maxMemory = maxMemory
        self.isScanning = isScanning
        self.cumulativeDifficulty = cumulativeDifficulty
        self.numberOfAssets = numberOfAssets
        self.freeMemory = freeMemory
        self.availableProcessors = availableProcessors
        self.totalEffectiveBalanceNXT = totalEffectiveBalanceNXT
        self.numberOfAccounts = numberOfAccounts
        self.numberOfBlocks = numberOfBlocks
        self.requestProcessingTime = requestProcessingTime
        self.version = version
        self.numberOfBidOrders = numberOfBidOrders
        self.lastBlock = lastBlock
        self.totalMemory = totalMemory
        self.application = application
        self.numberOfAliases = numberOfAliases
        self.lastBlockchainFeederHeight = lastBlockchainFeederHeight
        self.numberOfTrades = numberOfTrades
        self.time = time
        self.numberOfAskOrders = numberOfAskOrders
        self.lastBlockchainFeeder = lastBlockchainFeeder

class Time(BaseModel):
    def __init__(
            self,
            time=None,
            requestProcessingTime=None):
        self.time = time
        self.requestProcessingTime = requestProcessingTime