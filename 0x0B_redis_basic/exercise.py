#!/usr/bin/env python3
""" Main file """


import redis
import uuid
from typing import Union, Callable, Optional


class Cache():
    """Cache class"""
    def __init__(self) -> None:
        """ Initialize method """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
        if fn:
            return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """ Get method """


    def get_int(self, key: str) -> int:
        """ Get method """
