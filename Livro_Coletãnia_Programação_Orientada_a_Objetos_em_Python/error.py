class Erro001(Exception):
    pass

def erro():
    raise Erro001('Ação não permitida!')

try:
    erro()
except Erro001 as message:
    print(f'Erro: {message}')