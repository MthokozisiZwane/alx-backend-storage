#!/usr/bin/env python3
"""
Redis Basic
"""

import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


class Cache:
    """
    Cache class to interact with Redis for.
    """

    def __init__(self) -> None:
        """
        Initializes Cache with Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and return the generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[Any], Any] = None) -> Union[
            str, bytes, int, float]:
        """
        Retrieve data from Redis using the given key.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis using the given key and converts it to a
        string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis using the key and convert it to an integer.
        """
        return self.get(key, fn=int)

    def count_calls(func):
        """
        Counts the number of times a method is called.
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            method_name = func.__qualname__
            self._redis.incr(method_name)
            return func(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis, counting the number of calls.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def call_history(method):
        """
        Decorator to store input and output history of a method in Redis.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"
            self._redis.rpush(input_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(output_key, result)
            return result
        return wrapper

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and track input and output history.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


def replay(func):
    """
    Function to replay the history of calls of a particular function.
    """
    method_name = func.__qualname__
    inputs = cache._redis.lrange(f"{method_name}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method_name}(*{inp}) -> {out.decode('utf-8')}")


if __name__ == "__main__":
    cache = Cache()
