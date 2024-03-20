from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_1 = Restaurante('restaurante python', 'fastFood')
restaurante_2 = Restaurante('restaurante java', 'pizza express')
restaurante_3 = Restaurante('restaurante javaScript', 'comida japonesa')
restaurante_4 = Restaurante('restaurante ruby', 'comida tailandesa')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_pao = Prato('pãozinho', 3.0, 'Moreninho')


def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == "__main__":
    main()