from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pytest

url = "https://www.saucedemo.com/"
url_produtos = 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def setUp():
    driver = Chrome()
    driver.get(url)
    yield driver
    driver.quit()
    
@pytest.fixture
def login_app(setUp):
    driver = setUp
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    assert driver.current_url == url_produtos, 'URL incorreta!'
    yield driver