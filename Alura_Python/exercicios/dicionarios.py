"""1 - Para criar um dicionário com informações de uma pessoa, você pode utilizar a seguinte solução:"""
pessoa = {'nome': 'carlos', 'idade': 38, 'cidade': 'Petrolina'}

"""2 - Para fazer a atualização de um valor, adicionar um item e remover uma informação, você pode usar o seguinte raciocínio:"""
# Atualização de Idade
pessoa['idade'] = 39

# Adicionando Profissão
pessoa['profissao'] = 'Encarregado'

# Remoção de Elemento
# del pessoa['cidade']
# del pessoa['nome']

# print(pessoa)
"""3 - Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:"""
numeros = {x: x**2 for x in range(1, 6)}
print(numeros)

"""4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:"""
if 'nome' in pessoa: 
    print(f"A chave 'nome' existe no dicionário")
else:
    print(f"A chave 'nome' não existe no dicionário")

"""5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:"""
frase = "Python se tornou uma programação das linguagens de programação mais Python populares do mundo se programação nos Python últimos anos linguagens"
cont_palavras = {}
palavras = frase.split()
for palavra in palavras:
    cont_palavras[palavra] = cont_palavras.get(palavra, 0) +1
for key, value in cont_palavras.items():
    print(f'A palavra {key} exite {value} vezes')