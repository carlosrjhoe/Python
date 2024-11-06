from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    invalid_password = "1111111111"
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"

    def __init__(self, driver):
        self.driver = driver
        self.user_name_input = (By.XPATH, '//input[@id="user-name"]')
        self.password_input = (By.XPATH, '//input[@id="password"]')
        self.login_button = (By.XPATH, '//input[@id="login-button"]')
        self.erro_message = (
            By.XPATH, '//div[@class="error-message-container error"]')

    def open(self):
        self.driver.get(self.URL)

    def login(self):
        self.driver.find_element(
            *self.user_name_input).send_keys(self.username)
        self.driver.find_element(*self.password_input).send_keys(self.password)
        self.driver.find_element(*self.login_button).click()

    def invalid_login(self):
        self.driver.find_element(
            *self.user_name_input).send_keys(self.username)
        self.driver.find_element(
            *self.password_input).send_keys(self.invalid_password)
        self.driver.find_element(*self.login_button).click()
        return self.driver.find_element(*self.erro_message)

    def verify_login_error_message(self):
        return self.driver.find_element(*self.erro_message).text == self.expected_error_message
