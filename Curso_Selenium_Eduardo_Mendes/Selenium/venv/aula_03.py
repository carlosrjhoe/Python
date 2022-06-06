from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
driver = Chrome()
driver.get(url)
sleep(2)

a = driver.find_element(By.TAG_NAME, 'a')
p = driver.find_element(By.TAG_NAME, 'p')
print(f'Texto de a: {a.text}')
print(f'texto de p: {p.text}')

driver.close()