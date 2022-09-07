frequencia = {}

texto = 'Se alguma coisa pode dar errado, dará errado, e mais, dara errado da pior maneira, no pior momento e de modo que cause o maior / pior dano possível'

for palavra in texto.split():
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
    
palavra = frequencia.keys()

for i in palavra:
    print(f'{i} = {frequencia[i]}')