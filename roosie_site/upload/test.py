"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    def test_home(self):
        """Tests the home page."""
        response = self.client.get('')
        print(response)
        self.assertContains(response, 'Home', 0, 200)

    def test_books(self):
        """Tests the books page."""
        response = self.client.get('/%5Ebooks')
        self.assertContains(response, 'books', 1, 200)

    def test_lifts(self):
        """Tests the lifts page."""
        response = self.client.get('/%5Elifts')
        self.assertContains(response, 'lifts', 1, 200)

    def test_games(self):
        """Tests the games page."""
        response = self.client.get('/%5Egames')
        self.assertContains(response, 'games', 2, 200)
