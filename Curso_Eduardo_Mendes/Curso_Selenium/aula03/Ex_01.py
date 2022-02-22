from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

driver = Chrome()
driver.get(url)
sleep(3)

lista = []
for i in range(3):
    p = driver.find_elements_by_tag_name('p')
    lista.append(p[i].text)
print(lista)
driver.close()
