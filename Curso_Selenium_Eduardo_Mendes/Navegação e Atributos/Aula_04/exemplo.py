from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://selenium.dunossauro.live/aula_04_a.html')
lista_nao_ordenada = driver.find_elements(By.TAG_NAME, "ul") # 1
# 1. Buscamos 'ul'
lis = lista_nao_ordenada.find_elements(By.TAG_NAME, "li") # 2
# 2. Buscamos todos 'li'
lis[0].find_element(By. TAG_NAME, "a")
# 3. No primeiro 'li', buscamos 'a' e pegamos seu text.