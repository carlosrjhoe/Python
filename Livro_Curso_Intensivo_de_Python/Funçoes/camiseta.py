"""8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. A
função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem
estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados."""


def camisa_pequena(tamanho, msg):
    print(f'Tamanho da camisa: {tamanho}\nA frase da estampa: {msg}')
    
def camisa_media(tamanho='M', msg='Eu amo Python'):
    print(f'Tamanho da camisa {tamanho}\nA frase da estampa: {msg}')
    
def camisa_grande(tamanho='G', msg='Eu sou do time Java'):
    print(f'Tamanho da camisa {tamanho}\nA frase da estampa: {msg}')
    
    
camisa_pequena('P', 'A vida é bruta')
camisa_media()
camisa_grande()