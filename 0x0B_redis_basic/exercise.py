#!/usr/bin/env python3
""" Main file """


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count calls of method"""
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """counter for count"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return counter


class Cache():
    """Cache class"""
    def __init__(self) -> None:
        """ Initialize method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""

        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float]:
        """ Get method """
        data = self._redis.get(key)

        if fn:
            return fn(data)

        if fn is None:
            return data

    def get_str(self, key: str) -> str:
        """ Get method """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Get method """
        return self.get(key, int)
