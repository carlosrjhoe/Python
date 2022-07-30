from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")

procurar = driver.find_element(By.CLASS_NAME, 'search-field').send_keys('lambda')
butao = driver.find_element(By.CLASS_NAME, 'search-button').click()