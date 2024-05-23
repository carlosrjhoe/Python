class Test4:

    def test_adicionar_produto_no_carrinho(self, login_app):
        login_page = login_app
        login_page.clicar_em_produto()
        produto_escolhido = login_app.verificar_produto()
        produto_carrinho = login_page.abrir_carrinho()
        assert produto_escolhido == produto_carrinho, 'O produto não é o mesmo!!!'