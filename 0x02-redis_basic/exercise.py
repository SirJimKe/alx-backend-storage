#!/usr/bin/env python3
"""Redis Module"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initializes a Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis with a randomly generated key.
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
