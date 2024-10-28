import pytest
from pages.products_page import ProductsPage

def test_add_product_to_shopping_cart(setUp):
    object_page = ProductsPage(setUp)
    object_page.open()
    object_page.login()
    object_page.choose_product()
    assert object_page.check_shopping_cart() == '1'