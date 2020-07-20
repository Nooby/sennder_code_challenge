#!/usr/bin/env python3
import os

from app import app
from app.main import ghibli
from app.cache import RedisCache

if __name__ == "__main__":
    redis_host = os.environ.get("REDIS_HOST")
    if redis_host:
        redis_port = os.environ.get("REDIS_PORT")
        cache_ttl = os.environ.get("CACHE_TTL")
        cache = RedisCache(redis_host, redis_port, cache_ttl)
        ghibli._set_cache(cache)
    app.run(host='0.0.0.0', port=8000)
