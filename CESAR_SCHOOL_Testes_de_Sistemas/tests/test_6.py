from time import sleep

class Test6():

    def test_finalizar_compra_com_sucesso(self, login_app):
        checkout_page = login_app
        checkout_page.clicar_em_produto()
        checkout_page.verificar_produto()
        checkout_page.abrir_carrinho()
        checkout_page.realizar_checkout()
        checkout_page.clicar_botao_continue()
        checkout_page.preencher_campos_de_checkout_e_concluir_compra()
        assert checkout_page.verificar_compra_realizada_com_sucesso()