from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .login_page import LoginPage
from random import choice
from time import sleep


class ProductsPage(LoginPage):
    def __init__(self, driver):
        self.driver = driver
        self.products_title = (By.XPATH, '//span[@class="title"]')
        self.product_list = (By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
        self.product = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        self.shopping_cart = (By.XPATH, '//span[@class="shopping_cart_badge"]')
        super().__init__(driver)


    def is_products_title_dispayed(self):
        return self.driver.find_element(*self.products_title).text

    def choose_product(self):
        elements = self.driver.find_elements(*self.product_list)
        chosen_element = choice(elements)
        chosen_element.click()

    def check_shopping_cart(self):
        wait = WebDriverWait(self.driver, 5)
        quantity = wait.until(EC.visibility_of_element_located(self.shopping_cart))
        return quantity.text
