class Calculo_hora_extra():
    
    def __init__(self):
        # Construtor/inicializador
        self.valor_hora = 29.11 # Atributo default
        self.valor_hora_extra = 5.00 # Atributo default
        texto = 'Programa que gera o valor de salário de funcionários'
        print(f'{"#"*len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#"*len(texto)}')
       
    def calculo_de_horas(self):
        self.horas = int(input('Digite o valor das horas trabalhadas: '))
        self.adicional = int(input('Digite o valor das horas extras: ')) * self.valor_hora_extra
        self.hora_total = self.horas * self.valor_hora
        
    def exibe_dados(self):
        if float(self.horas < 40.00):
            print(f'Salário base: R${self.hora_total}')
        else:
            print(f'Salário base: R${self.hora_total}\nAdicional de horas extras: R${self.adicional:.2f}\nRemuneração total: R${self.hora_total+self.adicional}')
        
carlos = Calculo_hora_extra()
carlos.calculo_de_horas()
carlos.exibe_dados()