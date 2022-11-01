from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = Chrome()
url = 'https://clientes.sensorweb.com.br/ache/login.htm'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="user-input"]').send_keys('Klebson.luiz')
driver.find_element(By.XPATH, '//*[@id="password-input"]').send_keys('Teste007')
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/table/tbody/tr[2]/td[3]/input').click()
driver.find_element(By.XPATH, '//*[@id="icon-grafic"]').click()

driver.find_element(By.XPATH, '//*[@id="526"]/td[2]/a/span').click()


# driver.find_element('xpath', '//*[@id="icon-grafic"]').click()
