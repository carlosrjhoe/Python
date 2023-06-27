"""18 – Crie duas funções, mostra_numeros( ) e mostra_textos( ), que exibem em tela via função print( ) números e letras, respectivamente, a partir de um contêiner de dados ou função geradora. Utilize a biblioteca threading para executar essas duas funções em threads separadas:"""

import threading

def mostra_numeros():
    for i in range(1, 11):
        print(f'{i}')

def mostra_texto():
    letras = ['a', 'b', 'c', 'd', 'e']
    for letra in letras:
        print(f'{letra}')

if __name__ == '__main__':
    t1 = threading.Thread(target=mostra_numeros)
    t2 = threading.Thread(target=mostra_texto)

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    