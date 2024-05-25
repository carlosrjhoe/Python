from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class PaginaProdutos(LoginPage):

    def __init__(self) -> None:
        super().__init__()

    def filtar_produtos_do_menor_para_maior(self):
        self.driver.find