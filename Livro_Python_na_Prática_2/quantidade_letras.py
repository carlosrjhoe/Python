def verifica_letras_minusculas(texto):
    minusculas = []
    for letra in texto:
        if (letra.islower()):
            minusculas.append(letra)
    return minusculas

def verifica_letras_maiusculas(texto):
    maiusculas = []
    for letra in texto:
        if (letra.isupper()):
            maiusculas.append(letra)
    return maiusculas

def informacao(texto, verifica_letras_minusculas, verifica_letras_maiusculas):
    print(f'No nome {texto}, foram encontardos {len(verifica_letras_minusculas(texto))} letras minusculas: \n{verifica_letras_minusculas(texto)}')
    print(f'No nome {texto}, foram encotrados {len(verifica_letras_maiusculas(texto))} maiusculas: \n{verifica_letras_maiusculas(texto)}')
    return

if __name__ == "__main__":
    texto = 'Mayara Ramos Cordeiro'
    informacao(texto, verifica_letras_minusculas, verifica_letras_maiusculas)