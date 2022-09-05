texto = 'Código morse'
print(f'{"#" *len(texto)}')
print(f'{texto.center(len(texto))}')
print(f'{"#" *len(texto)}')


def codigo_morse(texto):
    codigo = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....',
        'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-',
        'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '·----', '2': '··---', '3': '···--',
        '4': '····-', '5': '·····', '6': '-····',
        '7': '--···', '8': '---··', '9': '----·',
        '0': '-----', '.': '·-·-·-', ',': '--··--',
        '?': '··--··', '!': '-·-·--', '/': '-··-·', '-': '-····-'
    }
    return ' '.join(codigo[i] for i in texto.upper())

texto = input('Digite o texto a ser convertido em código morse: ')
conversor = codigo_morse(texto)
print(f'{texto} em código morse: {conversor}')

