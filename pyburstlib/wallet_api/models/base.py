'''
pyburstlib
:author: drownedcoast
:date: 3-23-2018
'''
import json
from pyburstlib.exceptions import PyBurstLibException

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
        return json.dumps(self.__dict__)\

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def _model(class_):
        '''
        :param class_: The class that the value should be an instance of.
        :return: A decorator that ensures the assigning value is of `class_` instances.
        '''
        assert issubclass(class_, BaseModel)

        def decorator(f):
            def wrapper(self, model):
                if isinstance(model, class_):
                    f(self, model)
                elif isinstance(model, dict):
                    f(self, class_.from_dict(model))
                elif model is None:
                    f(self, None)
                else:
                    raise PyBurstLibException(u'Invalid value type.')
            return wrapper
        return decorator

    @staticmethod
    def _model_list(class_):
        '''
        :param class_: The class that elements should be an instance of.
        :return: A decorator that ensures the assigning value is a list of `class_` instances.
        '''
        assert issubclass(class_, BaseModel)

        def decorator(f):
            def wrapper(self, list_):
                if isinstance(list_, list):
                    model_list = []
                    for item in list_:
                        if isinstance(item, class_):
                            model_list.append(item)
                        elif isinstance(item, dict):
                            model_list.append(class_.from_dict(item))
                        else:
                            raise PyBurstLibException(u'Invalid element type.')
                    f(self, model_list)
                else:
                    f(self, [])
            return wrapper
        return decorator
