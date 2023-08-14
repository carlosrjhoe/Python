from selenium.webdriver import Chrome
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_uma_lista_e_recupera(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('To-Do', self.driver.title)
        self.fail('Teste finalizado')


if __name__ == '__main__':
    unittest.main(warnings='ignore')