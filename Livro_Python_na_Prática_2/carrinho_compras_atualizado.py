"""Implemente um sistema de carrinho com inserção e remoção de elementos via comando, da forma mais reduzida possível, porém sem fazer uso de compreensão de listas ou funções vazias, apenas estruturas condicionais simples. O sistema deve se manter ativo até que o usuário digite um comando para sair.
"""

def cabecalho():
    texto_1 = 'Digite o nome do produto e pressione [ENTER] para inserir no carrinho.'
    texto_2 = 'Digite [CORRIGE] para remover o último item inserido.'
    texto_3 = 'Digite SAIR para fechar o carrinho de compras.'
    
    print('#'*len(texto_1))
    print(texto_1.center(len(texto_1)))
    print(texto_2.center(len(texto_1)))
    print(texto_3.center(len(texto_1)))
    print('#'*len(texto_1))

def insercao_remocao():
    carrinho = []
    while (objeto := input('Digite um objeto: ')) != 'sair':
        carrinho.append(objeto.capitalize());print(f'Adicionando...{carrinho[-1]}\n{carrinho}')
        if objeto == 'corrige':
            del(carrinho[-2]);del(carrinho[-1]);print(carrinho)
    print(f'Lista final dos itens no carrinho: {carrinho}')
        

if __name__ == '__main__':
    cabecalho()
    insercao_remocao()

# ###################################################################### #
# Digite o nome do produto e pressione [ENTER] para inserir no carrinho. #
#         Digite [CORRIGE] para remover o último item inserido.          #
#             Digite SAIR para fechar o carrinho de compras.             #
# ###################################################################### #
# Digite um objeto: leite                                                #
# Adicionando...Leite                                                    #
# ['Leite']                                                              #
# Digite um objeto: pão                                                  #
# Adicionando...Pão                                                      #
# ['Leite', 'Pão']                                                       #
# Digite um objeto: mortadela                                            #
# Adicionando...Mortadela                                                #
# ['Leite', 'Pão', 'Mortadela']                                          #
# Digite um objeto: café                                                 #
# Adicionando...Café                                                     #
# ['Leite', 'Pão', 'Mortadela', 'Café']                                  #
# Digite um objeto: sair                                                 #
# Lista final dos itens no carrinho: ['Leite','Pão','Mortadela','Café']  #                                                         