def letrasMinusculas(texto):
    minusculas = [letra for letra in texto if letra.islower()]
    return minusculas

def letrasMaiusculas(texto):
    maiusculas = [letra for letra in texto if letra.isupper()]
    return maiusculas

def informacao(texto, letrasMinusculas, letrasMaiusculas):
    print(f'No nome {texto}, foram encontrados {len(letrasMinusculas(texto))} letras minusculas: \n{letrasMinusculas(texto)}')
    print(f'No nome {texto}, foram encontrados {len(letrasMaiusculas(texto))} maiusculas: \n{letrasMaiusculas(texto)}')
    return

if __name__ == '__main__':
    texto = 'Carlos Roberto Conceição Júnior'
    informacao(texto, letrasMinusculas, letrasMaiusculas)   