from django.test import TestCase
from django.urls import resolve
from .views import index

# Create your tests here.
class HomePageTest_2(TestCase):

    def test_root_url_lists(self):
        found = resolve('/lists_2/')
        self.assertEqual(found.func, index)