from collections import defaultdict
import requests

_base_url = "https://ghibliapi.herokuapp.com"


class Ghibli():

    def _get(self, url, **params):
        r = requests.get(_base_url + url, params=params)
        return r.json()

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
