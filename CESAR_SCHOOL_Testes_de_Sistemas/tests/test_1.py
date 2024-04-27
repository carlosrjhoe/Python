from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pytest

class Test_login:
    url = "https://www.saucedemo.com/"
    url_produtos = 'https://www.saucedemo.com/inventory.html'

    @pytest.fixture
    def setUp(self):
        self.driver = Chrome()
        self.driver.get(self.url)
        yield
        self.driver.quit()
        
    def test_abrir_browser_e_clicar_no_botao_login(self, setUp):
        """Abrir browser e clicar no botão login, e verifica se permanece na mesmo browser."""
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        assert self.driver.current_url == self.url, 'URL incorreta!'

    def test_clicar_no_botao_login_e_mostrar_msg_de_erro(self, setUp):
        """Clicar no botão login, e deve aparecer uma msg de erro."""
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        error_message = self.driver.find_element(By.CLASS_NAME, 'error-message-container')
        assert error_message.text == 'Epic sadface: Username is required', "Messagem de erro incorreta!"

    def test_efetuar_login_valido_e_deve_exibir_pagina_de_produtos(self, setUp):
        """Efetuar login valido e deve exibir pagina de produtos"""
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        assert self.driver.current_url == self.url_produtos, 'URL incorreta!'