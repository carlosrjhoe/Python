from cgitb import text
from contextlib import closing
from typing import Text
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
driver = Chrome()
driver.get(url)
sleep(3)

a = driver.find_element(By.TAG_NAME, 'a')

print(f'Texto de a: {a.text}')

for click in range(11):
    # Buscar um elemento
    ps = driver.find_elements(By.TAG_NAME, 'p')
    # Clicar em um elemento
    a.click()
    # Pegar o valor do elemento
    print(f'texto de p: {int(ps[-1].text)}, valor do click: {click}')
    # Verifirar variaveis
    print({ps[-1].text} == {Text(click)})

driver.close()