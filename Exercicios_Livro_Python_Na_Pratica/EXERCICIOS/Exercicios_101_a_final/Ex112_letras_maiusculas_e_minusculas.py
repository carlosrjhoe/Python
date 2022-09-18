class Verifica_letras:

    def __init__(self) -> None:
        texto = 'Programa que verifica quantidades de letras maiusculas e minusculas'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.maiusculas = 0
        self.minusculas = 0
        self.informe_texto = input('Digite um texto: ')
        
    def letras_maiusculas(self):
        for letra in self.informe_texto:
            if letra.isupper():
                self.maiusculas += 1
    
    def letras_minusculas(self):
        for letra in self.informe_texto:
            if letra.islower():
                self.minusculas += 1
                
    def exibir_informacoes(self):
        print(f'No texto {self.informe_texto}\nTem {self.maiusculas} letras maisculas e {self.minusculas} minusculas')