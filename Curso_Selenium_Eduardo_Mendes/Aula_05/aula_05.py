from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = "https://www.hashtagtreinamentos.com/curso-python"
driver = Chrome()
driver.get(url)

driver.find_element('xpath', '//*[@id="_form_1919_"]/div[1]/div[1]/div/input').send_keys('Carlos Roberto')
driver.find_element('xpath', '//*[@id="_form_1919_"]/div[1]/div[2]/div/input').send_keys('carlosrjhoe@gmail.com')
driver.find_element('xpath', '//*[@id="_form_1919_submit"]').click()