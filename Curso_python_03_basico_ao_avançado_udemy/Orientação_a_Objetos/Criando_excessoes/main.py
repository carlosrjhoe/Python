class TaErrado(Exception):
    pass 

def testar():
    raise TaErrado('Errado')

try:
    testar()
except TaErrado as erro:
    print(f'Erro: {erro}')