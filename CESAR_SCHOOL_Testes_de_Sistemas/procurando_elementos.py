import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from random import choice
from time import sleep


url = "https://www.saucedemo.com/"
url_produtos = 'https://www.saucedemo.com/inventory.html'
nome = 'standard_user'
senha = 'secret_sauce'

driver = Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element(By.NAME, 'user-name').send_keys(nome)
driver.find_element(By.NAME, 'password').send_keys(senha)
driver.find_element(By.NAME, 'login-button').click()
produto = driver.find_elements(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
item = random.choice(produto)
sleep(5)
item.click()

    
# driver.close()

# numeros = [1, 2, 3, 4, 5]
# item = choice(numeros)
# print(item)