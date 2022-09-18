class Verificar_positivos_e_negativos:
    
    def __init__(self) -> None:
        texto = 'Programa irá verificar os numeros positivos e negativos'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.lista = [-1,6,-9,-8,4,0,-3,2,7,1,8,-2]
        print(f'LISTA ORIGINAL: {self.lista}')
        
    def verificar_negativo(self):
        self.lista_negativos = [x for x in self.lista if x < 0]
        return self.lista_negativos
    
    def verificar_positivos(self):
        self.lista_positivos = [x for x in self.lista if x >= 0]
        return self.lista_positivos

    def exibe_informacao(self):
        print(f'Lista de números NEGATIVOS: {self.lista_negativos}')
        print(f'lista de números POSITIVOS: {self.lista_positivos}')