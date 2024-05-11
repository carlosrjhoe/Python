from conftest import url, url_produtos

class Test_login:
    
    def test_abrir_browser(self, setUp):
        """AAbrir browser e verificar se é um url válido"""
        login_page = setUp
        assert login_page.is_url_login(), 'URL incorreta!'

    def test_clicar_no_botao_login_e_mostrar_msg_de_erro(self, setUp):
        """Clicar no botão login, e deve aparecer uma msg de erro."""
        login_page = setUp
        login_page.login_button()
        assert login_page.has_message_login_message_error() == 'Epic sadface: Username is required'

    def test_efetuar_login_valido_e_deve_exibir_pagina_de_produtos(self, setUp):
        """Efetuar login valido e deve exibir pagina de produtos"""
        login_page = setUp
        assert login_page.executar_login_valido() == 'Products'
        