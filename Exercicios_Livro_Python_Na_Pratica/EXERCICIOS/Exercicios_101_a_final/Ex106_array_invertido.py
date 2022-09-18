from array import array


class Inverter:
    
    def __init__(self) -> None:
        texto = 'Programa para inverter um array'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.numeros = array('i', [4,10,15,20,25,30,35,40])
        
    def array_invertido(self):
        print('Array na sequência original.')
        for i in self.numeros:
            print(f'{i}', end=' ')
        self.numeros.reverse()
        print('\nArray na sequência invertida.')
        for i in self.numeros:
            print(f'{i}', end=' ')