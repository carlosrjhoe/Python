from django.test import TestCase
from django.urls import reverse
from animais.views import index

class AnimaisUrlsTestCase(TestCase):

    def test_rota_url_ultiliza_view_index(self):
        '''Teste home principal do App animais'''
        root = reverse('/')
        self.assertEqual(root.func, index)