"""Como exportar dados de um DataFrame para um arquivo CSV?"""
"""data = {'Nome': ['Alice', 'Bárbara', 'Carlos', 'Davi', 'Maria', 'Tânia', 'Eder', 'Fernando'],'Idade': [30, 33, 17, 35, 28, 60, 59, 35],'Gênero': ['Mulher', 'Mulher', 'Homem', 'Homem', 'Mulher', 'Mulher', 'Homem', 'Homem'],'Profissão': ['Médica', 'Médica', 'Estudante', 'Professor', 'Advogada', 'Aposentada', 'Empresário', 'Estudante'],'Salário': [32000, 25000, 1300, 5000, 10000, 6000, 10000, 7000]}"""

import pandas as pd

def expor_dados_CSV(dicionario):
    df = pd.DataFrame(dicionario)
    df.to_csv('arquivo_dados.csv', index= False)
    

if __name__ == '__main__':
    data = {
        'Nome': ['Alice', 'Bárbara', 'Carlos', 'Davi', 'Maria', 'Tânia', 'Eder', 'Fernando'],
        'Idade': [30, 33, 17, 35, 28, 60, 59, 35],
        'Gênero': ['Mulher', 'Mulher', 'Homem', 'Homem', 'Mulher', 'Mulher', 'Homem', 'Homem'],
        'Profissão': ['Médica', 'Médica', 'Estudante', 'Professor', 'Advogada', 'Aposentada', 'Empresário', 'Estudante'],
        'Salário': [32000, 25000, 1300, 5000, 10000, 6000, 10000, 7000]}

    expor_dados_CSV(data)