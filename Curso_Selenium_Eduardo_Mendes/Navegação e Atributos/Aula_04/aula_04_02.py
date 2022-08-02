from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://selenium.dunossauro.live/aula_04_a.html')

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
    
def find_by_href(driver, link):
    """Encontrar o elemnto com o texto "text".
    
    Arguments:
        - driver = Instância do driver Chrome.add()
        - link = link que será procurado em todos as tag's "a".
    """
    
    elementos = driver.find_elements(By.TAG_NAME, 'a')
    
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento
    

# elemento_ddg = find_by_text(driver, "li", "DuckDuckGo")
elemento_ddg = find_by_href(driver, 'ddg')