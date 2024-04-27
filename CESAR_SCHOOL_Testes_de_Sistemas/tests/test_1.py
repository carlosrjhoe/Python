from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def test_abrir_browser_e_clicar_no_botao_login():
    driver = Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, "login-button").click()
