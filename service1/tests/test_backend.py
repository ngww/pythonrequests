from unittest.mock import patch
import requests

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_generate(self):
        with patch('requests.get') as a:
            with patch('requests.post') as n:
                a.return_value.text = "dog"
                n.return_value.text = "woof"

                response = self.client.get(url_for('generate'))
                self.assertEqual(response.status_code, 200)