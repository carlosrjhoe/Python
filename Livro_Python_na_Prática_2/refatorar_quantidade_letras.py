def letras_minusculas(texto):
    minusculas = [letra for letra in texto if letra.islower()]
    return minusculas

def letras_maiusculas(texto):
    maiusculas = [letra for letra in texto if letra.isupper()]
    return maiusculas

def informacao(texto, letras_minusculas, letras_maiusculas):
    print(f'No nome {texto}, foram encontardos {len(letras_minusculas(texto))} letras minusculas: \n{letras_minusculas(texto)}')
    print(f'No nome {texto}, foram encotrados {len(letras_maiusculas(texto))} maiusculas: \n{letras_maiusculas(texto)}')
    return

if __name__ == '__main__':
    texto = 'Carlos Roberto Conceição Júnior'
    informacao(texto, letras_minusculas, letras_maiusculas)