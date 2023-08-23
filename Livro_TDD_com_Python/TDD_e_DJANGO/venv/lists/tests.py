from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from .views import index

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_lists_2(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_return_corret_html(self):
        response = self.client.get('/')
        html = response.content.decode('UTF-8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>')
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'lists.html')
