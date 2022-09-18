from datetime import datetime


class Verificar_calendario:
    
    def __init__(self) -> None:
        texto = 'Programa irá verificar quantidade de segundas-feiras'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
        
        self.segundas = 0
        self.meses = range(1,13)
        
    def verificar_ano(self):
        for ano in range(2010, 2021):
            for mes in self.meses:
                if datetime(ano, mes, 1).weekday() == 0:
                    self.segundas += 1
                    
    def exibe_informacao(self):
        print(f'Entre 2010 e 2022, exitem {self.segundas} segundas-feiras no primeiro dia do mês.')