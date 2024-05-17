from pages.login_page import LoginPage

class Test_logout(LoginPage):

    def test_logout(self, setUp):
        logout_page = setUp
        logout_page.executar_login_valido()
        logout_page.clicar_barra_de_menu()
        assert logout_page.is_url_login()