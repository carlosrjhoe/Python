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
    
    # Cria um dicionário vázio
    resultados = {}
    # Este método localizará o elemento em uma página e atribuir em uma variável
    elemento = driver.find_element(By.TAG_NAME, "main") 
    # Este método encontrar vários elementos, e retornar uma lista e atribui na variável
    main_ancoras = elemento.find_elements(By.TAG_NAME, 'a') 
    
    for ancora in main_ancoras:
        # Este método tentará primeiro retornar o valor de uma propriedade com o nome fornecido.
        resultados[ancora.text] = ancora.get_attribute('href') 
        
    # Este método navegará até um link selecionado
    driver.get(resultados['Exercício 3']) 
    
    
pegar_todos_os_elementos(driver, 'main')