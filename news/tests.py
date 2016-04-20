from django.test import TestCase
from django.utils.translation import get_language

class Test(TestCase):
    def test_some(self):
        print get_language()
