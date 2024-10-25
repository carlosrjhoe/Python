import pytest
from pages.login_page import PaginaLogin
from pages.produto_page import PaginaProduto


def test_login_com_sucesso(setUp):
    login_page = PaginaLogin(setUp)
    pagina_produto = PaginaProduto(setUp)
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    assert pagina_produto.exibir_titulo_produtos()
