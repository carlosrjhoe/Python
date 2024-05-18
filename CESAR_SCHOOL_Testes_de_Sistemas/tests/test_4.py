class Test4:

    def test_adicionar_produto_no_carrinho(self, login_app):
        login_page = login_app
        qtd = login_page.clicar_em_produto()
        assert qtd == 6