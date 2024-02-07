from excessoes import MeuError, levantar
from notas_excessoes import levantar

try:
    levantar()
except MeuError as erro:
    print(f'{erro.__class__.__name__}')
    print(f'{erro.args}')