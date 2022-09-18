from array import array


class Transformar:
    
    def __init__(self) -> None:
        texto = 'Programa para transformar uma lista em array.'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.lista = array('i',[1,3,5,7,8,9,11,13,15,16,17,21,31,52,64,85])
        
    def exibir_array(self):
        print(f'A lista é composta de {len(self.lista)} elementos.')
        print(f'A lista possui um tamanho de {self.lista.itemsize} bytes')
        print(f'A lista está alocada na memória do endereço {self.lista.buffer_info()[0]}')