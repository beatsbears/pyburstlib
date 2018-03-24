'''
pyburstlib
:author: drownedcoast
:date: 3-23-2018
'''
import json

class BaseModel(object):

    @classmethod
    def from_json(cls, j):
        return cls.from_dict(json.loads(j))

    @classmethod
    def from_dict(cls, dict_):
        instance = cls()
        for key in dict_:
            setattr(instance, key, dict_[key])
        return instance

    def to_json(self):
        return json.dumps(self.__dict__)
