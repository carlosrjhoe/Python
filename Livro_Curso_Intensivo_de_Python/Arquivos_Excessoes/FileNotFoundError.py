"""Um problema comum ao trabalhar com arquivos é o tratamento de arquivos ausentes."""

file_name = 'carlos.txt'

try:
    if file_name:
        with open(file_name) as object:
            contents = object.read()
            print(contents)
except FileNotFoundError:
    msg = 'Desculpe, o arquivo carlos.txt não existe.'
    print(f'{msg}')
