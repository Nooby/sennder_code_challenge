import json
from collections import defaultdict

import requests

from app.cache import DummyCache

_base_url = "https://ghibliapi.herokuapp.com"


class Ghibli():

    def __init__(self):
        self._cache = DummyCache()

    def _get(self, url, **params):
        # TODO: Take params into consideration in cache key.
        cached = self._cache.get(url)
        if cached:
            return json.loads(cached)
        r = requests.get(_base_url + url, params=params)
        self._cache.set(url, r.text)
        return json.loads(r.text)

    def _set_cache(self, cache):
        assert cache
        self._cache = cache

    def films(self):
        """Films retrieves all available ghibli movies as JSON."""
        return self._get("/films", limit=250)

    def people(self):
        """People retrieves all available ghibli characters
        sorted into their movies."""
        people_lookup = defaultdict(lambda: [])
        people = self._get("/people", limit=250)
        for p in people:
            for film in p['films']:
                filmID = film.split('/')[-1]
                people_lookup[filmID].append(p)
        return people_lookup
