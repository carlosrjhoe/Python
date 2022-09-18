from array import array


class Criar_array:
    
    def __init__(self) -> None:
        texto = 'Programa irar gerar um array e verificar se cada numero do array é PAR'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.numeros = array('i', [4,10,15,20,25,30,35,40])
        
    def exibir_array(self):
        for i in self.numeros:
            if i % 2 == 0:
                print(f'{i} é um numero par!')