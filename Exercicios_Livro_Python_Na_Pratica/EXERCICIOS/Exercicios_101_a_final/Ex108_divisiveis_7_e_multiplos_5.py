class Divisiveis_Multiplos:
    
    def __init__(self) -> None:
        texto = 'Programa irá verificar números divisiveis por 7 e multimplos de 5.'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.numeros = []
        
    def divisiveis_multiplos(self):
        for numero in range(0, 501):
            if (numero % 7 == 0) and (numero % 5 == 0):
                self.numeros.append(str(numero))
    
    def exibir(self):
        print(f'{",".join(self.numeros)}')