from selenium.webdriver.common.by import By


class PaginaLogin():
    URL_SAUCEDEMO = 'https://www.saucedemo.com/'

    def __init__(self, webdriver):
        self.driver = webdriver
        self.user_name = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def open(self):
        self.driver.get(self.URL_SAUCEDEMO)

    def login(self, user_name, password):
        self.driver.find_element(*self.user_name).send_keys(user_name)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
