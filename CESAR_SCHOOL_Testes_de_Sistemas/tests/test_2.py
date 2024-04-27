from selenium.webdriver.common.by import By
from conftest import url

class Test_logout:

    def test_logout(self, login_app):
        driver = login_app
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()
        assert driver.current_url == url, 'URL incorreta!'