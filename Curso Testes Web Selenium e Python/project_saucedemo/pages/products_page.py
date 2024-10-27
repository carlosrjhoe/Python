from selenium.webdriver.common.by import By
from .login_page import LoginPage


class ProductsPage(LoginPage):
    def __init__(self, driver):
        self.driver = driver
        self.products_title = (By.XPATH, '//span[@class="title"]')
        super().__init__(driver)


    def is_products_title_dispayed(self):
        return self.driver.find_element(*self.products_title).text
        