from modelos.restaurante import Restaurante

restaurante_1 = Restaurante('restaurante python', 'fastFood')
restaurante_1.receber_avaliacao('carlos', 10)
restaurante_1.receber_avaliacao('mayara', 8)
restaurante_1.receber_avaliacao('neto', 7)
restaurante_2 = Restaurante('restaurante java', 'pizza express')
restaurante_2.receber_avaliacao('carlos', 5)
restaurante_2.receber_avaliacao('mayara', 10)
restaurante_2.receber_avaliacao('neto', 2)
restaurante_3 = Restaurante('restaurante javaScript', 'comida japonesa')
restaurante_3.receber_avaliacao('carlos', 9)
restaurante_3.receber_avaliacao('mayara', 3)
restaurante_3.receber_avaliacao('neto', 7)
restaurante_4 = Restaurante('restaurante ruby', 'comida tailandesa')
restaurante_4.receber_avaliacao('carlos', 7)
restaurante_4.receber_avaliacao('mayara', 2)
restaurante_4.receber_avaliacao('neto', 5)


def main():
    restaurante_1.alterar_estado()
    restaurante_3.alterar_estado()
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()