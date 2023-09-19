from django.test import LiveServerTestCase
from selenium.webdriver import Chrome

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        '''Configurar ambiente de testes'''
        self.driver = Chrome('chromedriver.exe')

    def tearDown(self) -> None:
        self.driver.quit()