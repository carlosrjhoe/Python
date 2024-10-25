from selenium.webdriver.common.by import By


class PaginaProduto():
    def __init__(self, webdriver):
        self.driver = webdriver
        self.product = (
            By.XPATH, '//*[@class="inventory_item"][1]')
        self.botao_produto = (By.XPATH, "//*[text()='Add to cart']")
        self.carrinho_produto = (By.XPATH, "//*[@class='shopping_cart_link']")
        self.titulo_produto = (By.XPATH, "//span[@class='title']")

    def exibir_titulo_produtos(self):
        titulo = self.driver.find_element(*self.titulo_produto).is_displayed()
        return titulo

    def escolher_produto(self):
        self.driver.find_element(*self.product).click()
        self.driver.find_element(*self.botao_produto).click()
        self.driver.find_element(*self.carrinho_produto).click()
        produto = self.driver.find_element(*self.produto)
        return produto.text
