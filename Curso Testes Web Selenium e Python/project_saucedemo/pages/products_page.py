from selenium.webdriver.common.by import By


class ProductsPage():
    def __init__(self, driver):
        self.driver = driver
        self.products_title = (By.XPATH, '//span[@class="title"]')


    def is_products_title_dispayed(self):
        return self.driver.find_element(*self.products_title).text
        