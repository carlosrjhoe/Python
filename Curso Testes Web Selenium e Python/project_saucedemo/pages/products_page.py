from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .login_page import LoginPage
from random import choice


class ProductsPage(LoginPage):
    def __init__(self, driver):
        self.driver = driver
        self.products_title = (By.XPATH, '//span[@class="title"]')
        self.product_list = (
            By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
        self.product = (
            By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
        self.shopping_cart = (By.XPATH, '//span[@class="shopping_cart_badge"]')
        self.shopping_cart_button = (By.XPATH, '//a[@class="shopping_cart_link"]')
        self.shopping_cart_iventory_button = (
            By.XPATH, '//a[@class="shopping_cart_link"]')
        self.shopping_cart_item = (
            By.XPATH, '//div[@class="inventory_item_name"]')
        self.iventory_items = (
            By.XPATH, '//div[@class="inventory_item_name "]')
        self.iventory_item_button = (By.XPATH, '//button[@id="add-to-cart"]')
        self.inventory_item_name = (
            By.XPATH, '//div[@data-test="inventory-item-name"]')
        super().__init__(driver)

    def is_products_title_dispayed(self):
        return self.driver.find_element(*self.products_title).text

    def choose_product(self):
        elements = self.driver.find_elements(*self.product_list)
        chosen_element = choice(elements)
        chosen_element.click()

    def choose_inventory_item_name(self):
        items = self.driver.find_elements(*self.iventory_items)
        chosen_item = choice(items)
        chosen_item.click()

    def get_inventory_item_name(self):
        item = self.driver.find_element(*self.inventory_item_name).text
        return item

    def click_iventory_item_button(self):
        return self.driver.find_element(*self.iventory_item_button).click()

    def click_shopping_cart_inventory_button(self):
        return self.driver.find_element(*self.shopping_cart_iventory_button).click()

    def click_shopping_cart(self):
        return self.driver.find_element(*self.shopping_cart_button).click()

    def get_shopping_cart_item_name(self):
        return self.driver.find_element(*self.shopping_cart_item).text

    def check_shopping_cart(self):
        wait = WebDriverWait(self.driver, 5)
        quantity = wait.until(
            EC.visibility_of_element_located(self.shopping_cart))
        return quantity.text
