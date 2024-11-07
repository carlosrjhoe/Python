import pytest
from pages.products_page import ProductsPage
# from time import sleep

def test_add_product_to_shopping_cart(setUp):
    product_page = ProductsPage(setUp)
    product_page.open()
    product_page.login()
    product_page.choose_product()
    assert product_page.check_shopping_cart() == '1'

def test_verify_the_product_name_in_the_cart(setUp):
    product_page = ProductsPage(setUp)
    product_page.open()
    product_page.login()
    product_page.choose_inventory_item_name()
    product_name = product_page.get_inventory_item_name()
    product_page.click_iventory_item_button()
    product_page.click_shopping_cart_inventory_button()
    product_shopping_cart_name = product_page.get_shopping_cart_item_name()
    assert product_name == product_shopping_cart_name