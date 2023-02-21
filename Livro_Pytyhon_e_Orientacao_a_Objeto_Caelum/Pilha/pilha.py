"""Para adicionarmos um elemento ao topo da pilha podemos
usar o nosso já conhecido .append( ) recebendo o novo elemento
como parâmetro."""

pilha = [10,20,30]

"""Adicionando um elemento ao topo de pilha"""
pilha.append(40)
print(pilha)

"""Removendo um elemento do topo(último a ser incerido) da pilha"""
pilha.pop()
print(pilha)

"""Consultando o tamanho da pilha"""
tamanho_da_pilha = len(pilha)
print(tamanho_da_pilha)