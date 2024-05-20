import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:
    url = "https://www.saucedemo.com/"
    url_produtos = 'https://www.saucedemo.com/inventory.html'
    
    def open_login_page(self):
        self.driver = Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

    def realizar_logout(self):
        self.driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_message_login_message_error(self):
        mensage_erro = self.driver.find_element(By.CLASS_NAME, 'error-message-container')
        return mensage_erro.text

    def login_button(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def executar_login_valido(self):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        produto_titulo = self.driver.find_element(By.XPATH, "//span[@class='title']")
        return produto_titulo.text

    def clicar_barra_de_menu(self):
        self.driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()

    def clicar_em_produto(self):
        lista_produtos = self.driver.find_elements(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
        item = random.choice(lista_produtos)
        item.click()

    def abrir_carrinho(self):
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()        

        
    def close_login_page(self):
        self.driver.quit()