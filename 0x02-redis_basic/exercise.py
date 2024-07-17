#!/usr/bin/env python3
"""
writes strings to redis
"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count the number of calls to a function"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """ init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ strore data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes], Union[str, int, float]]] = None
            ) -> Union[str, int, float, None]:
        """Get data from redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """ gets string data from redis"""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """ gets int dat from redis """
        return self.get(key, int)
