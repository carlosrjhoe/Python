from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://selenium.dunossauro.live/aula_04_b.html')

def find_by_text(driver, tag, text):
    """Encontrar o elemnto com o texto "text".
    
    Arguments:
        - driver = Instância do driver Chrome.add()
        - texto = Conteúdo que deve está na tag.
        - tag = tag onde o texto será procurado.
    """
    
    elementos = driver.find_elements(By.TAG_NAME, tag)
    
    for elemento in elementos:
        if elemento.text == text:
            return elemento

lista = ['um', 'dois', 'tres', 'quatro']

for texto in lista:
    elemento = find_by_text(driver, 'div', texto).click()