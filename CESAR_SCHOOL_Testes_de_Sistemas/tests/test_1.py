from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

def test_abrir_browser_e_clicar_no_botao_login():
    """Abrir browser e clicar no botão login, e verifica se permanece na mesmo browser."""
    url = "https://www.saucedemo.com/"
    driver = Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    assert driver.current_url == url, 'URL incorreta!'

def test_clicar_no_botao_login_e_mostrar_msg_de_erro():
    """Clicar no botão login, e deve aparecer uma msg de erro."""
    url = "https://www.saucedemo.com/"
    driver = Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container')
    assert error_message.text == 'Epic sadface: Username is required', "Messagem de erro incorreta!"
    driver.quit()
