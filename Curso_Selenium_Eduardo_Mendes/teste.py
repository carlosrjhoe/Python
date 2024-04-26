from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By


driver = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_03.html#'
driver.get(url)
sleep(1)

for i in range(1, 6):
    driver.find_element(By.TAG_NAME, 'a').click()
    elements = (driver.find_elements(By.TAG_NAME, 'p'))
    print(f'Valor de ultimo p: {elements[-1].text} valor do click: {i}')
    



