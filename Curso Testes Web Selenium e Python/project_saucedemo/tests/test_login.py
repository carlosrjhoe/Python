import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.login
def test_login_sucess(setUp):
    login_page = LoginPage(setUp)
    Object_product_page = ProductsPage(setUp)
    login_page.open()
    login_page.login()
    assert Object_product_page.is_products_title_dispayed() == "Products"

@pytest.mark.login
def test_invalid_login(setUp):
    login_page = LoginPage(setUp)
    login_page.open()
    assert login_page.invalid_login()