from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://selenium.dunossauro.live/aula_04_a.html')
lista_nao_ordenada = driver.find_element_by_tag_name('ul') # 1
lis = lista_nao_ordenada.find_element_by_tag_name('li') # 2
lis[0].find_element_by_tag_name('a') # 3

"""
1. Buscamos 'ul'
2. Buscamos todos 'li'
3. No primeiro 'li', buscamos 'a' e pegamos seu text.
"""