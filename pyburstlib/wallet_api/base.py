'''
pyburstlib
:author: drownedcoast
:date: 3-22-2018
'''
import json 
class BaseApi(object):

    def __init__(self, client):
        self._client = client

class BaseRequest(object):

    def as_payload(self):
        return json.dumps(self.__dict__)