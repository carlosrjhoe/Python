"""abrir arquivo"""
# arquivo = open('monty_python_song.txt')
# leitura = arquivo.read()
# print(leitura)

"""Escrita de arquivo"""
# arquivo = open('novo_arquivo.txt', 'w')
# arquivo.write('novo conteudo.\n')
# arquivo.write('novo conteudo 1.\n')
# arquivo.write('novo conteudo 2.\n')
# arquivo.write('novo conteudo 3.\n')
# arquivo.close()

"""Lista com writelines"""
# ingredientes = ['ovo', 'conteudo', 'batata', 'novo', 'cenoura', 'novo']
# ingredientes = [item+'\n' for item in ingredientes]
# arq = open('ingredientes.txt', 'w')
# arq.writelines(ingredientes)
# arq.close()

# Comando with
# with open('monty_python_song.txt') as musica:
#     for linha in musica:
#         print(linha)


# ingredientes = ['ovo', 'conteudo', 'batata', 'novo', 'cenoura', 'novo']
# with open('acai.txt', 'w') as acai:
#     for item in ingredientes:
#         acai.write(item + '\n')

# Modulo math
# from math import *
# print(pow(2, 3))
# print(ceil(2.1))
# print(floor(2.8))
# print(trunc(1.8))
# print(round(1.9))
# print(pi)

# Modulo OS
# import os
"""deletar arquivo"""
# # os.remove('acai.txt')
# # if os.path.exists('acai.txt'):
# #     print('exite')
# # else:
# #     print('Não existe')

# Randon
# import random
# # print(random.randint(1, 10))
# nomes = ['carlos', 'may', 'neto', 'luna', 'valdenia', 'valeria', 'davi', 'rosicler', 'emilly']
# """escolher nome"""
# # print(random.choice(nomes))
# """embaralhar lista"""
# random.shuffle(nomes)
# print(nomes)

# Orientação a Objeto
class Pessoa:
    def __init__(self, nome, idade, endereco='Av Eraldo Barros de Souza N°166 CASA "C"') -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __repr__(self) -> str:
        return f'Nome: {self.nome.title()}\nIdade: {self.idade}\nEnd: {self.endereco}\n{"=-"*25}'
    
if __name__ == "__main__":
    p1 = Pessoa('carlos', 38)
    p2 = Pessoa('mayara', 39)
    print(p1)
    print(p2)