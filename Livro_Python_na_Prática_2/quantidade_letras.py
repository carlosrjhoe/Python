def verificaLetrasMinusculas(texto):
    minusculas = []
    for letra in texto:
        if (letra.islower()):
            minusculas.append(letra)
    return minusculas

def verificaLetrasMaiusculas(texto):
    maiusculas = []
    for letra in texto:
        if (letra.isupper()):
            maiusculas.append(letra)
    return maiusculas

def informacao(texto, verificaLetrasMinusculas, verificaLetrasMaiusculas):
    print(f'No nome {texto}, foram encontardos {len(verificaLetrasMinusculas(texto))} letras minusculas: \n{verificaLetrasMinusculas(texto)}')
    print(f'No nome {texto}, foram encotrados {len(verificaLetrasMaiusculas(texto))} maiusculas: \n{verificaLetrasMaiusculas(texto)}')
    return

if __name__ == "__main__":
    texto = 'Carlos Roberto Conceição Júnior'
    informacao(texto, verificaLetrasMinusculas, verificaLetrasMaiusculas)