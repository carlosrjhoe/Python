from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
url_saucedemo = 'https://www.saucedemo.com/'
driver.get(url_saucedemo)

user_name = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')
botao = driver.find_element(By.ID, 'login-button')

user_name.send_keys('standard_user')
password.send_keys('secret_sauce')
botao.click()