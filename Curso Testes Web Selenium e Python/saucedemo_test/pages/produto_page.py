from selenium.webdriver.common.by import By


class PaginaProduto():
    def __init__(self, webdriver):
        self.driver = webdriver
        self.titulo_produto = (By.XPATH, "//span[@class='title']")

    def exibir_titulo_produtos(self):
        titulo = self.driver.find_element(*self.titulo_produto).text
        return titulo
