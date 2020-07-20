import redis


class DummyCache():

    def set(self, key, value):
        return True

    def get(self, key):
        return None


class RedisCache():

    def __init__(self, host, port, ttl=60):
        self._redis = redis.Redis(host=host, port=port)
        self._ttl = ttl

    def _set_redis(self, redis):
        assert redis
        self._redis = redis

    def set(self, key, value):
        """ Set adds a key value pair to the cache."""
        setResp = self._redis.set(key, value.encode("utf-8"))
        self._redis.expire(key, self._ttl)
        return setResp

    def get(self, key):
        """ Get retrieves the value of the given key from cache."""
        getResp = self._redis.get(key)
        if getResp:
            getResp = getResp.decode("utf-8")
        return getResp
