from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


url = "https://www.saucedemo.com/"
url_produtos = 'https://www.saucedemo.com/inventory.html'
nome = 'standard_user'
senha = 'secret_sauce'

driver = Chrome()
driver.get(url)
driver.find_element(By.NAME, 'user-name').send_keys(nome)
driver.find_element(By.NAME, 'password').send_keys(senha)
driver.find_element(By.NAME, 'login-button').click()
lista_produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")
print(len(lista_produtos))
    
driver.close()
    