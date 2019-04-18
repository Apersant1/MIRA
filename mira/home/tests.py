from django.test import TestCase

from django.urls import resolve
from .views import home


class NewTest(TestCase):
    def test_can(self):

        found = resolve('/')
        self.assertEqual(found.func, home)
