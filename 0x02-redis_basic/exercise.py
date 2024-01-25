#!/usr/bin/env python3
"""Redis Module"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    def __init__(self):
        """
        Initializes a Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis with a randomly generated key.
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """
        Retrieves the data stored in Redis under the given key
        """
        data = self._redis.get(key)

        if data is not None and fn is not None:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves and returns a string from Redis under the given key.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves and returns an integer from Redis under the given key.
        """
        return self.get(key, fn=int)
