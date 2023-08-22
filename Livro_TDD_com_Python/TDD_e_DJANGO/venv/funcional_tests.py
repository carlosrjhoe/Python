from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_uma_lista_e_recupera(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('To-Do', self.driver.title)
        
        heade_text = self.driver.find_element(By.TAG_NAME,'h1')
        self.assertIn('To-Do', heade_text)
        
        inputbox = self.driver.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        sleep(1)

        table = self.driver.find_element(By.ID,'id_list_table')
        rows = table.find_element(By.TAG_NAME,'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers') for row in rows
        )
        
        self.fail('Teste finalizado')


if __name__ == '__main__':
    unittest.main()