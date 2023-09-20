from django.test import LiveServerTestCase
from selenium.webdriver import Chrome

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        '''Abrir Webdriver'''
        self.driver = Chrome()

    def tearDown(self) -> None:
        '''Fechar Webdriver'''
        self.driver.quit()

    def test_para_verificar_janela_webdriver_esta_ok(self):
        self.driver.get(self.live_server_url)

    def test_deu_errado(self):
        '''Teste de exemplo de erro'''
        self.fail('Teste falhou...')

    def test_buscando_um_novo_animal(self):
        '''Teste buscar animal na pesquisa'''
        