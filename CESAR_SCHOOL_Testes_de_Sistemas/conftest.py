from selenium.webdriver import Chrome
import pytest

url = "https://www.saucedemo.com/"
url_produtos = 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def setUp():
    driver = Chrome()
    driver.get(url)
    yield driver
    driver.quit()