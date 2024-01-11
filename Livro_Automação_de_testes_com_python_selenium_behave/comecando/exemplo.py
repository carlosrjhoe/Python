from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

url = 'https://www.google.com/'
driver.get(url)
titulo_site = 'Automação de Testes com Python, Selenium e Behave - Pesquisa Google'
element = driver.find_element(By.NAME, 'q')
element.send_keys('Automação de Testes com Python, Selenium e Behave')
element.submit()

try:
    assert titulo_site in driver.title
    print(f'Título do site correto')

except Exception as erro:
    print(f'Título do site incorreto', erro)
driver.quit()