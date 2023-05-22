"""A partir de uma simples base de dados em uma lista, composta por ['1001','1002','1003','1004','1005','1006',None,'1008','1009'], gere uma nova base de dados a partir desta contendo apenas dados válidos. Retorne ao usuário uma mensagem informando a posição de índice do dado inválido da base de dados original.
"""

def verificacao_lista(lista_original, lista_validada, invalido):
    for i in lista_original:
        if i is not None:
            lista_validada.append(i)
        else:
            invalido = lista_original.index(None)
    
    print(f'Lista original: {lista_original}\nNova lista: {lista_validada}\nExiste um dado inválido no índice {invalido} na lista original.')
    

if __name__ == "__main__":
    invalido = 0
    lista_validada = []
    lista_original = ['1001','1002','1003','1004','1005','1006',None,'1008','1009']
    verificacao_lista(lista_original, lista_validada, invalido)
    
