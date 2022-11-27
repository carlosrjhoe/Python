from usuarios import usuarios
from datetime import datetime
ano = datetime.now().year


for kye, lista in usuarios.items():
    print(f'\nDados de {kye.title()}:')
    print(f'\tNome: {lista["primeiro_nome"].title()}')
    print(f'\tSobrenome: {lista["segundo_nome"].title()}')
    print(f'\tNascimento: {lista["nascimento"]}')
    print(f'\tIdade: {ano - int(lista["nascimento"])}')
    print(f'\tCidade natal: {lista["cidade"].title()}')
    
    
