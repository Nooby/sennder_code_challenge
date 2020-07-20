import unittest
from unittest.mock import MagicMock

import requests_mock

from app.ghibli import Ghibli
from app.cache import DummyCache


test_data_films = '''
[
  {
    "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
    "title": "Castle in the Sky",
    "description": "The orphan Sheeta inherited a mysterious crystal...",
    "director": "Hayao Miyazaki",
    "producer": "Isao Takahata",
    "release_date": "1986",
    "rt_score": "95",
    "people": [
      "https://ghibliapi.herokuapp.com/people/"
    ],
    "species": [
      "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
    ],
    "locations": [
      "https://ghibliapi.herokuapp.com/locations/"
    ],
    "vehicles": [
      "https://ghibliapi.herokuapp.com/vehicles/"
    ],
    "url": "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
  },
  {
    "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
    "title": "Grave of the Fireflies",
    "description": "In the latter part of World War II,...",
    "director": "Isao Takahata",
    "producer": "Toru Hara",
    "release_date": "1988",
    "rt_score": "97",
    "people": [
      "https://ghibliapi.herokuapp.com/people/"
    ],
    "species": [
      "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
    ],
    "locations": [
      "https://ghibliapi.herokuapp.com/locations/"
    ],
    "vehicles": [
      "https://ghibliapi.herokuapp.com/vehicles/"
    ],
    "url": "https://ghibliapi.herokuapp.com/films/12cfb892-aac0-4c5b-94af-521852e46d6a"
  }
]
'''


test_data_people = '''
[
  {
    "id": "ba924631-068e-4436-b6de-f3283fa848f0",
    "name": "Ashitaka",
    "gender": "Male",
    "age": "late teens",
    "eye_color": "Brown",
    "hair_color": "Brown",
    "films": [
      "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
    ],
    "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
    "url": "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"
  },
  {
    "id": "ebe40383-aad2-4208-90ab-698f00c581ab",
    "name": "San",
    "gender": "Female",
    "age": "17",
    "eye_color": "Brown",
    "hair_color": "Brown",
    "films": [
      "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
    ],
    "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
    "url": "https://ghibliapi.herokuapp.com/people/ebe40383-aad2-4208-90ab-698f00c581ab"
  },
  {
    "id": "87b68b97-3774-495b-bf80-495a5f3e672d",
    "name": "Yasuko Kusakabe",
    "gender": "Female",
    "age": "Adult",
    "eye_color": "Brown",
    "hair_color": "Dark Brown",
    "films": [
      "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
    ],
    "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
    "url": "https://ghibliapi.herokuapp.com/people/87b68b97-3774-495b-bf80-495a5f3e672d"
  }
]
'''


class TestGhibliFilms(unittest.TestCase):

    TEST_URL = "https://ghibliapi.herokuapp.com/films"

    @requests_mock.Mocker()
    def test_films(self, m):
        # Arange
        g = Ghibli()
        m.get(self.TEST_URL, text=test_data_films)
        # Act
        f = g.films()
        # Assert
        self.assertEqual(len(f), 2)
        self.assertEqual(f[0]['title'], "Castle in the Sky")
        self.assertEqual(f[1]['title'], "Grave of the Fireflies")

    @requests_mock.Mocker()
    def test_films_cached(self, m):
        # Arange
        g = Ghibli()
        m.get(self.TEST_URL, text="")
        mockCache = DummyCache()
        mockCache.get = MagicMock(return_value=test_data_films)
        g._set_cache(mockCache)
        # Act
        f = g.films()
        # Assert
        self.assertEqual(len(f), 2)
        self.assertEqual(f[0]['title'], "Castle in the Sky")
        self.assertEqual(f[1]['title'], "Grave of the Fireflies")


class TestGhibliPeople(unittest.TestCase):

    TEST_URL = "https://ghibliapi.herokuapp.com/people"

    @requests_mock.Mocker()
    def test_people(self, m):
        # Arange
        g = Ghibli()
        m.get(self.TEST_URL, text=test_data_people)
        # Act
        f = g.people()
        # Assert
        self.assertEqual(len(f), 2)
        self.assertEqual(len(f['0440483e-ca0e-4120-8c50-4c8cd9b965d6']), 2)
        self.assertEqual(len(f['58611129-2dbc-4a81-a72f-77ddfc1b1b49']), 1)

    @requests_mock.Mocker()
    def test_people_cache(self, m):
        # Arange
        g = Ghibli()
        m.get(self.TEST_URL, text="")
        mockCache = DummyCache()
        mockCache.get = MagicMock(return_value=test_data_people)
        g._set_cache(mockCache)
        # Act
        f = g.people()
        # Assert
        self.assertEqual(len(f), 2)
        self.assertEqual(len(f['0440483e-ca0e-4120-8c50-4c8cd9b965d6']), 2)
        self.assertEqual(len(f['58611129-2dbc-4a81-a72f-77ddfc1b1b49']), 1)
