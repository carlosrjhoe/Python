import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

url = "https://www.saucedemo.com/"
url_produtos = 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def setUp():
    login_page = LoginPage()
    login_page.open_login_page()
    yield login_page
    login_page.close_login_page()
    
@pytest.fixture
def login_app(setUp):
    login_page = setUp
    login_page.executar_login_valido()
    # login_page.open_login_page()
    # login_page.find_element(By.ID, "user-name").send_keys("standard_user")
    # login_page.find_element(By.XPATH, "//*[@id='login-button']").click()
    assert login_page.current_url == url_produtos, 'URL incorreta!'
    yield login_page

# # Essa parte do código é para escolher o tivo de browser
# @pytest.fixture
# def pytest_addoption(parser):
#   parser.addoption('--browser_selenium', default='chrome', help= 'Select a browser')

# @pytest.fixture
# def browser(request):
#     selected_browser = request.config..getoption('--browser_selenium')
#     yeld