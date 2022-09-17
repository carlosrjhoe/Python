class Prova:
    
    def __init__(self) -> None:
        self.nota = ''
        
        texto = 'Exercicio validação de notas'
        print(f'{"#" * len(texto)}')
        print(f'{texto.center(len(texto))}')
        print(f'{"#" * len(texto)}')
        
    def primeiro_semestre(self):
        self.nota = float(input('Digite sua nota: '))
        
    def validacao(self):
        if self.nota < 0 or self.nota > 1.0:
            print('Pontuação invalida\nA nota deve ser um valor entre 0 e 1.0')
        elif self.nota == 1.0:
            print('Parabéns, você gabaritou a prova!')
        elif self.nota >= 0.6:
            print('Parabéns você foi aprovado!')
        elif self.nota < 0.6:
            print('Nota a baixo da média, você está em recuperação.')
        else:
            print('Não foi peossível computar sua nota...')

try:
    prova = Prova()
    prova.primeiro_semestre()
    prova.validacao()
except ValueError as erro:
    print('valor inválido...\nDigite apenas números')
    quit()