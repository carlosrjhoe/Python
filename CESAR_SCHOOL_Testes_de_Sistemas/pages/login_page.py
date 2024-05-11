from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage:
    url = "https://www.saucedemo.com/"
    url_produtos = 'https://www.saucedemo.com/inventory.html'
    
    def open_login_page(self):
        self.driver = Chrome()
        self.driver.get(self.url)

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_message_login_message_error(self):
        mensage_erro = self.driver.find_element(By.CLASS_NAME, 'error-message-container')
        return mensage_erro.text

    def login_button(self):
        self.driver.find_element(By.ID, 'login-button').click()

    def executar_login_valido(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        produto_titulo = self.driver.find_element(By.CLASS_NAME, "title")
        return produto_titulo.text

    def clicar_barra_de_menu(self):
        # //*[@id="menu_button_container"]
        self.driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        
    def close_login_page(self):
        self.driver.quit()