from selenium.webdriver import Chrome

driver = Chrome()
url = 'https://clientes.sensorweb.com.br/ache/login.htm'
driver.get(url)

driver.find_element('xpath', '//*[@id="user-input"]').send_keys('Klebson.luiz')

driver.find_element('xpath', '//*[@id="password-input"]').send_keys('Teste007')

driver.find_element('xpath', '/html/body/div[2]/div/div/div/form/table/tbody/tr[2]/td[3]/input').click()

driver.find_element('xpath', '//*[@id="icon-grafic"]').click()

driver.find_element('xpath', '/tr[@id="526"]/td/input').click()
driver.find_element('xpath', '/tr[@id="528"]/td/input').click()



# //*[@id="526"]/td[2]/a/span
# //*[@id="526"]/td[1]/input

# /html/body/div[6]/div[1]/div/div[3]/div/table[1]/tbody/tr[22]/td[1]/input
# //*[@id="526"]/td[1]/input
# /html/body/div[6]/div[1]/div/div[3]/div/table[1]/tbody/tr[25]/td[1]/input