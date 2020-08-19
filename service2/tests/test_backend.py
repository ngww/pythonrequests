from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_animals(self):
        response = self.client.get(url_for('animal'))
        self.assertEqual(response.status_code, 200)

    def test_dog(self):
        response = self.client.get(url_for('noise'), data="dog")
        self.assertIn(b'woof', response.data)

    def test_cat(self):
        response = self.client.get(url_for('noise'), data="cat")
        self.assertIn(b'meow', response.data)
    
    def test_horse(self):
        response = self.client.get(url_for('noise'), data="horse")
        self.assertIn(b'neigh', response.data)
    
    def test_cow(self):
        response = self.client.get(url_for('noise'), data="cow")
        self.assertIn(b'moo', response.data)

    def test_other(self):
    # We will mock a response of dog and test that we get woof returned.
        with patch('requests.get') as g:
            g.return_value.text = "goat"

            response = self.client.get(url_for('noise'))
            self.assertIn(b"Don't know what noise this animal makes", response.data)