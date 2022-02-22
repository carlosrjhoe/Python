from selenium.webdriver import Chrome # importa Selenium.webdriver
from time import sleep # Importa o modulo sleep da biblioteca 

url = 'https:/curso-python-selenium.netlify.app/aula_03.html'
driver = Chrome()
driver.get(url)
sleep(1)

a = driver.find_element_by_tag_name('a')

for click in range(11):
    ps = driver.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor de p: {ps[-1].text} Valor do click: {click}')
    print(f'Os valores são iguais {ps[-1].text == str(click)}')
driver.quit()
