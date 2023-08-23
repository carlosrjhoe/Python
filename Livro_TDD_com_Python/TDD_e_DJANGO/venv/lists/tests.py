from django.test import TestCase
from django.urls import resolve
from .views import index

# Create your tests here.
class HomePageTest(TestCase):

    def test_index_return_corret_html(self):
        # Chamar a view function de forma direta
        response = self.client.get('/')
        # Verificar qual template foi redenrizado
        self.assertTemplateUsed(response, 'lists/index.html')
