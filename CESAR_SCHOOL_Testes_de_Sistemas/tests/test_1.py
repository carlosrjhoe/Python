from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from conftest import url, url_produtos

class Test_login:
    
    def test_abrir_browser_e_clicar_no_botao_login(self, setUp):
        """Abrir browser e clicar no botão login, e verifica se permanece na mesmo browser."""
        driver = setUp
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        assert driver.current_url == url, 'URL incorreta!'

    def test_clicar_no_botao_login_e_mostrar_msg_de_erro(self, setUp):
        """Clicar no botão login, e deve aparecer uma msg de erro."""
        driver = setUp
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        error_message = driver.find_element(By.CLASS_NAME, 'error-message-container')
        assert error_message.text == 'Epic sadface: Username is required', "Messagem de erro incorreta!"

    def test_efetuar_login_valido_e_deve_exibir_pagina_de_produtos(self, setUp):
        """Efetuar login valido e deve exibir pagina de produtos"""
        driver = setUp
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        produto_titulo = driver.find_element(By.CLASS_NAME, "title")
        assert produto_titulo.text == "Products", 'Página não encontrada!'
        assert driver.current_url == url_produtos, 'URL incorreta!'