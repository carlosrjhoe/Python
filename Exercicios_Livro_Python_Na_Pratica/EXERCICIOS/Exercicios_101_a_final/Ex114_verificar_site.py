class Verificacao:

    def __init__(self) -> None:
        texto = 'Programa irá verificar endereço de site'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.endereco = ''
        
    def verificar_site(self):
        while ((self.endereco.startswith('www.') and self.endereco.endswith('.com.br'))) != True:
            self.endereco = input('Digite o endereço de site: ')
        print(f'{self.endereco} é um site válido!')