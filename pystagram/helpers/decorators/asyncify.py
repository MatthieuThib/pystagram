import asyncio
from functools import wraps
from types import FunctionType
from typing import Dict, Type, Any


# def asyncify(cls):
#     attrs = cls.__dict__.items().copy()
#     for attr_name, attr_value in attrs:
#         if isinstance(attr_value, FunctionType) and attr_name.startswith('__') is False:
#             setattr(cls, "async_" + attr_name, _asyncify(attr_value))
#     return cls


def asyncify(cls):
    class AsyncifiedClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for attr_name, attr_value in cls.__dict__.copy().items():
                if isinstance(attr_value, FunctionType) and attr_name.startswith('__') is False:
                    # delattr(cls, attr_name)
                    setattr(cls, attr_name, _asyncify(attr_value))
    return AsyncifiedClass




    # class WrappedClass(cls):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         for attr_name, attr_value in cls.__dict__.items():
    #             if isinstance(attr_value, FunctionType) and attr_name.startswith('__') is False:
    #                 del cls.__dict__[attr_name]
    #                 setattr(cls, "async_" + attr_name, _asyncify(attr_value))


#
def _asyncify(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        async def async_func(self, *args, **kwargs):
            return func(self, *args, **kwargs)

        return async_func(self, *args, **kwargs)
    return wrapper
#
#
# def asyncify(cls: Type):
#
#     def decorator(cls):
#         attrs: Dict[str, Any] = {}
#         for attr_name, attr_value in cls.__dict__.items():
#             if isinstance(attr_value, FunctionType) and attr_name.startswith('__') is False:
#                 attrs[attr_name] = _asyncify(attr_value)
#             else:
#                 attrs[attr_name] = attr_value
#         return type(cls.__class__.__name__, cls.__class__.__bases__, attrs)
#     return decorator
