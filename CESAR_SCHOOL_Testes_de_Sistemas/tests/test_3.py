from pages.login_page import LoginPage
from conftest import url

class Test_logout(LoginPage):

    def test_logout(self, setUp):
        logout_page = setUp
        logout_page.executar_login_valido()
        logout_page.clicar_barra_de_menu()
        logout_page.realizar_logout()
        assert logout_page.is_url_login()