from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_1 = Restaurante('restaurante python', 'fastFood')
restaurante_2 = Restaurante('restaurante java', 'pizza express')
restaurante_3 = Restaurante('restaurante javaScript', 'comida japonesa')
restaurante_4 = Restaurante('restaurante ruby', 'comida tailandesa')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('pãozinho', 3.0, 'Moreninho')
prato_pao.aplicar_desconto()
restaurante_1.adicionar_no_cardapio(bebida_suco)
restaurante_2.adicionar_no_cardapio(bebida_suco)
restaurante_3.adicionar_no_cardapio(bebida_suco)
restaurante_2.adicionar_no_cardapio(prato_pao)


def main():
    restaurante_1.exibir_cardapio
    restaurante_2.exibir_cardapio
    restaurante_3.exibir_cardapio

if __name__ == "__main__":
    main()