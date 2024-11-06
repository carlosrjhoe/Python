import pytest
from pages.products_page import ProductsPage

def test_add_product_to_shopping_cart(setUp):
    product_page = ProductsPage(setUp)
    product_page.open()
    product_page.login()
    product_page.choose_product()
    assert product_page.check_shopping_cart() == '1'
