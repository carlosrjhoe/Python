import pytest
from pages.login_page import PaginaLogin
from pages.produto_page import PaginaProduto


def test_login_com_sucesso(webdriver):
    login_page = PaginaLogin(webdriver)
    pagina_produto = PaginaProduto(webdriver)
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    assert pagina_produto.exibir_titulo_produtos()
