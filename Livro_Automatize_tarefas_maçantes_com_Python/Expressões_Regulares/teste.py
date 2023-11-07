def eNumeroDeTelefone(texto):
    """Verificar se a string em texto é um número de telefone válido"""
    if len(texto) != 13:
        return False
    for i in range(0, 3):
        if not texto[i].isdecimal():
            return False
    if texto[2] != '-':
        return False
    for i in range(3, 7):
        if not texto[i].isdecimal():
            return False
    if texto[8] != '-':
        return False
    for i in range(9, 12):
        if not texto[i].isdecimal():
            return False
    return True

if __name__ == '__main__':
    print('81-99541-9951 é um número válido?')
    print(eNumeroDeTelefone('81-99541-9951'))