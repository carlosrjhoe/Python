from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

campo = driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys('python')
# botao = driver.find_element(By.CLASS_NAME, 'gNO89b')