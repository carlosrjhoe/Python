from pprint import pprint
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

"""
    1. Pegar todos os links de aulas
        {'nome da aula': 'link da aula'}
    2. Nevegar até o exercício 03
        Achar a url do exercício 03 e ir até lá
"""

driver = Chrome()
driver.get('https://selenium.dunossauro.live/aula_04.html')

sleep(1)

def pegar_todos_os_elementos(driver, elemento):
    """Retornar um dicionario com os tag's e seus atrubutos de href"""
    resultados = {} # Cria um dicionário vázio
    elemento = driver.find_element(By.TAG_NAME, "main") # Este método localizará o elemento em uma página e atribuir em uma variável
    main_ancoras = elemento.find_elements(By.TAG_NAME, 'a') # Este método encontrar vários elementos, e retornar uma lista e atribui na variável
    
    for ancora in main_ancoras:
        resultados[ancora.text] = ancora.get_attribute('href') # Este método tentará primeiro retornar o valor de uma propriedade com o nome fornecido.
    
    driver.get(resultados['Exercício 3']) # Este método navegará até um link selecionado
    
    
pegar_todos_os_elementos(driver, 'main')