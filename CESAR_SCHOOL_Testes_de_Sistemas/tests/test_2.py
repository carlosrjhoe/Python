from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import url

class Test_logout:

    def test_logout(self, login_app):
        driver = login_app
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        menu_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.ID, "react-burger-menu-btn"))
        assert menu_element.is_displayed(), 'Menu não foi aberto!'
        
        driver.find_element(By.ID, "logout_sidebar_link").click()