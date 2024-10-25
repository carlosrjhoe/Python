import pytest
from pages.login_page import PaginaLogin
from pages.produto_page import PaginaProduto


def test_adicionar_produto_carrinho(setUp):
    login_produto_page = PaginaLogin(setUp)
    produto_page = PaginaProduto(setUp)
    login_produto_page.open()
    login_produto_page.login('standard_user', 'secret_sauce')
    produto_page.escolher_produto()
    
