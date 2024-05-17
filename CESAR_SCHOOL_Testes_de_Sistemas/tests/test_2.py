from pages.login_page import LoginPage

class Test3(LoginPage):

    def test_efetuar_login_valido_e_deve_exibir_pagina_de_produtos(self, setUp):
        """Efetuar login valido e deve exibir pagina de produtos"""
        login_page = setUp
        assert login_page.executar_login_valido() == 'Products'