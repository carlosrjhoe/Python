from modelos.restaurante import Restaurante

restaurante_1 = Restaurante('restaurante python', 'fastFood')
restaurante_2 = Restaurante('restaurante java', 'pizza express')
restaurante_3 = Restaurante('restaurante javaScript', 'comida japonesa')
restaurante_4 = Restaurante('restaurante ruby', 'comida tailandesa')


def main():
    restaurante_1.alterar_estado()
    restaurante_3.alterar_estado()
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()