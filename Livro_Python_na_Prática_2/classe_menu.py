'''Supondo que para um determinado propósito temos uma classe de nome Menu, que quando instanciada recebe um dado / valor que deve obrigatoriamente ser de tipo numérico para criação de seu respectivo objeto / atributo de classe. A validação por sua vez deve ocorrer a partir do método construtor da classe.
'''

import numbers

class Menu:
    def __init__(self, num):
        if isinstance(num, numbers.Number) and num > 0:
            '''Verifica se o numéro repassado é numérico e maior que 0'''
            self.num = num
        else:
            raise TypeError('Valor deve ser numérico e maior que zero.')
    

if __name__ == '__main__':
    maquina1 = Menu(5)
    maquina2 = Menu('cinco')