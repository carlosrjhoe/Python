"""7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete"""

enquete = {}
continua = True

while continua:
    nome = input('Diga seu nome: ')
    pergunta = input('Se pudesse visitar um lugar do mundo, para onde você iria? ')
    enquete[nome] = pergunta
    continuar = input('Deseja continuar? ').upper()
    
    if continuar == 'NAO':
        continua = False
        
print('Resultado da Enquete:')
for nome, resposta in enquete.items():
    print(f'{nome.title()}, {resposta.title()}')
    
    