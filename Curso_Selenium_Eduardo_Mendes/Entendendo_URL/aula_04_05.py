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
    elemento = driver.find_element(By.TAG_NAME, "main") # Procura e atribui o resultado a tag MAIN na variavel
    main_ancoras = elemento.find_elements(By.TAG_NAME, 'a') # Procura os elementos e atribui na variável
    
    for ancora in main_ancoras:
        resultados[ancora.text] = ancora.get_attribute('href')

    pprint(resultados)


pegar_todos_os_elementos(driver, 'main')