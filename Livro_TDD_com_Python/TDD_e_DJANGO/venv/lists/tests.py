from django.test import TestCase
from django.urls import resolve
from .views import index

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_lists_2(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_return_corret_html(self):
        # Chamar a view function de forma direta
        response = self.client.get('/')
        # Extrair bytes puro da resposta e converter o html em strigs 
        html = response.content.decode('UTF-8')
        # Verificar se a pagina é uma página padrão HTML
        self.assertTrue('<html>', html)
        # Verificar o titilo da pagina renderizada
        self.assertIn('<title>To-Do lists</title>', html)
        # Verificar qual template foi redenrizado
        self.assertTemplateUsed(response, 'lists/index.html')
