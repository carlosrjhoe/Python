from django.test import LiveServerTestCase
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        '''Abrir Webdriver'''
        self.driver = Chrome()

    def tearDown(self) -> None:
        '''Fechar Webdriver'''
        self.driver.quit()

    def test_buscando_um_novo_animal(self):
        '''Teste buscar animal na pesquisa'''
        # Ele encontra o Busca Animal e decide usar o site
        home_page = self.driver.get(self.live_server_url)
        
        # porque ele vê no menu do site escrito Busca Animal.
        nav_element = self.driver.find_element(By.CLASS_NAME, '.navbar')
        self.assertEqual('Busca Animal', nav_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome. 
        
        # Ele pesquisa por Leão e clica no botão pesquisar.

        # O site exibe 4 caracteristicas do animal pesquisado.
    
        # Ele desiste de adotar um leão.