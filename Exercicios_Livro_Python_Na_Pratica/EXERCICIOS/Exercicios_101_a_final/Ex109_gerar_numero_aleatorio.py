from random import randint


class Geracao:
    
    def __init__(self) -> None:
        texto = 'Programa irá gerar um número aleatório'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.numero_adivinhado = ''
        self.numero_gerado = randint(0, 11)
        
    def perguntar_numero(self):
        while self.numero_adivinhado != self.numero_gerado:
            self.numero_adivinhado = int(input('Adivinhe um número entra [0 e 10]: '))
        print(f'Parabéns, Você acertou!\nO número gerado foi {self.numero_gerado}')