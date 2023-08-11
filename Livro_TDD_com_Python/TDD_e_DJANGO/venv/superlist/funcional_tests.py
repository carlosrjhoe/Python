import unittest
from selenium.webdriver import Chrome

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.quit()

    def iniciar_uma_lista_e_recupera(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('To-Do', self.driver.title())
        self.fail('Teste finalizado')


if __name__ == '__main__':
    unittest.main(warnings='ignore')