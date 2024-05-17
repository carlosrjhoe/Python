class Test4:

    def test_adicionar_produto_no_carrinho(self, login_app):
        login_page = login_app
        login_page.executar_login_valido()
        login_page.clicar_barra_de_menu()
        # assert login_page.current_url == url_produtos, 'URL incorreta!'