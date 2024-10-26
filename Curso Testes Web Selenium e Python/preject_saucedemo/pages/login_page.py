from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def __init__(self, driver):
        self.driver = driver
        self.user_name_input = (By.XPATH, '//input[@id="user-name"]')
        self.password_input = (By.XPATH, '//input[@id="password"]')
        self.login_button = (By.XPATH, '//input[@id="login-button"]')

    def open(self):
        self.driver.get(self.URL)

    def login(self):
        self.driver.find_element(*self.user_name_input).send_keys(self.username)
        self.driver.find_element(*self.password_input).send_keys(self.password)
        self.driver.find_element(*self.login_button).click()
