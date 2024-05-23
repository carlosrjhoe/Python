from time import sleep


class Test5:

    def test_verificar_msg_erro_sem_preencher_dados_de_compra(self, login_app):
        login_page = login_app
        login_page.clicar_em_produto()
        login_app.verificar_produto()
        login_page.abrir_carrinho()
        login_app.realizar_checkout()
        login_app.clicar_botao_continue()
        assert login_app.has_message_login_message_error()