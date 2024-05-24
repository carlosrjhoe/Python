import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage:

    def __init__(self) -> None:
        self.user_name_field = (By.XPATH, "//*[@id='user-name']")
        self.password_field = (By.XPATH, "//*[@id='password']")
        self.button = (By.XPATH, "//*[@id='login-button']")
        self.url = "https://www.saucedemo.com/"
        self.url_produtos = 'https://www.saucedemo.com/inventory.html'
    
    def open_login_page(self):
        self.driver = Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

    def realizar_logout(self):
        elemento = WebDriverWait(self.driver, 1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        elemento.click()
        

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_message_login_message_error(self):
        mensage_erro = self.driver.find_element(By.CLASS_NAME, 'error-message-container')
        return mensage_erro.text

    def login_button(self):
        self.driver.find_element(*self.button).click()

    def executar_login_valido(self):
        self.driver.find_element(*self.user_name_field).send_keys("standard_user")
        self.driver.find_element(*self.password_field).send_keys("secret_sauce")
        self.driver.find_element(*self.button).click()
        produto_titulo = self.driver.find_element(By.XPATH, "//span[@class='title']")
        return produto_titulo.is_displayed()

    def clicar_barra_de_menu(self):
        self.driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()

    def clicar_em_produto(self):
        lista_produtos = self.driver.find_elements(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
        item = random.choice(lista_produtos)
        item.click()

    def verificar_produto(self):
        lista_produtos = self.driver.find_elements(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
        item = random.choice(lista_produtos)
        item.text

    def abrir_carrinho(self):
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()

    def verificar_1_item_do_carrinho(self):
        item = self.driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
        return item.text

    def realizar_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    def clicar_botao_continue(self):
        self.driver.find_element(By.ID, 'continue').click()

    def preencher_campos_de_checkout_e_concluir_compra(self):
        self.driver.find_element(By.ID, 'first-name').send_keys('nome_test')
        self.driver.find_element(By.ID, 'last-name').send_keys('sobre_nome_test')
        self.driver.find_element(By.ID, 'postal-code').send_keys('54515110')
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.ID, 'finish').click()

    def verificar_compra_realizada_com_sucesso(self):
        msg_sucesso = self.driver.find_element(By.XPATH, '//span[@class="title"]')
        return msg_sucesso.is_displayed()
        
    def close_login_page(self):
        self.driver.quit()