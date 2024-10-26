import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_login_sucess(setUp):
    Object_login_page = LoginPage(setUp)
    Object_product_page = ProductsPage(setUp)
    Object_login_page.open()
    Object_login_page.login()
    assert Object_product_page.is_products_title_dispayed() == 'Products'