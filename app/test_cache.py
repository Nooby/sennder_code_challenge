import unittest
from unittest.mock import patch

from app.cache import RedisCache


class TestRedisCache(unittest.TestCase):

    @patch('redis.Redis')
    def test_simple_set(self, redisMock):
        # Arrange
        redisMock.set.return_value = True
        redisMock.expire.return_value = True
        c = RedisCache("testHost", "6379")
        c._set_redis(redisMock)
        # Act
        ok = c.set("key", "Value")
        # Assert
        self.assertTrue(ok)
        redisMock.set.assert_called_once()
        redisMock.expire.assert_called_once()

    @patch('redis.Redis')
    def test_simple_get(self, redisMock):
        # Arrange
        redisMock.get.return_value = 'Hello'.encode('utf-8')
        c = RedisCache("testHost", "6379")
        c._set_redis(redisMock)
        # Act
        ok = c.get("key")
        # Assert
        self.assertTrue(ok)
        redisMock.get.assert_called_once()
