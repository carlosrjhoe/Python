def textoPositivo(texto):
    print(f'{texto} é um número válido!')
    
def eNumeroDeTelefone(texto):
    """Verificar se a string em texto é um número de telefone válido"""
    if len(texto) != 14:
        return False
    for i in range(0, 3):
        if not texto[i].isdecimal():
            return False
    if texto[3] != '-':
        return False
    for i in range(4, 9):
        if not texto[i].isdecimal():
            return False
    if texto[9] != '-':
        return False
    for i in range(10, 14):
        if not texto[i].isdecimal():
            return False
    textoPositivo(texto)

if __name__ == '__main__':
    textoPositivo('081-99541-9951')
    textoPositivo('081-98794-9484')