'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
from pyburstlib.wallet_api.models.base import BaseModel

class AccountRS(BaseModel):
    def __init__(
            self,
            accountRS=None,
            requestProcessingTime=None,
            account=None):
        self.accountRS = accountRS
        self.requestProcessingTime = requestProcessingTime
        self.account = account

class AccountLong(BaseModel):
    def __init__(
            self,
            stringId=None,
            requestProcessingTime=None,
            longId=None):
        self.stringId = stringId
        self.requestProcessingTime = requestProcessingTime
        self.longId = longId